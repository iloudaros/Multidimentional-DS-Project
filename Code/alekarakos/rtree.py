from point import Point
from box import Box
from math import fabs

"""
Implementation of an R-tree suitable for 3D data entries,
based on A. Guttman's R-tree paper:
'R-TREES. A DYNAMIC INDEX STRUCTURE
FOR SPATIAL SEARCHING', 1984
"""

# Define maximum and minimum entries a single node can contain.
MAX_ENTRIES = 8
MIN_ENTRIES = 2


class Entry:
    """
    Represents the data of each node. If the node is a leaf it contains a trajectory instance (x,y,t) else a pointer to a child node.
    """

    def __init__(self, child: "Node" = None, data: "Point" = None) -> "Entry":
        self.child = child
        self.data = data
        self.box = self.getEntryBox()

    def __str__(self) -> str:
        return f"Entry Box: {self.box}"

    def getEntryBox(self) -> "Box":
        """Sets the size of the minimum bounding box of the entry based on child node or data."""
        if self.child == None:
            # box size = point mbb
            return self.data.mbb
        return self.child.getMBB()


class Node:
    def __init__(self, parent: "Node" = None, entries: "Entry" = []) -> "Node":
        self.parent = parent
        self.entries = entries

        self.assignParent()

    def isRoot(self) -> bool:
        return self.parent == None

    def isLeaf(self) -> bool:
        if self.isRoot():
            return self.entries == [] or self.entries[0].data != None
        return self.entries[0].data != None

    def isFull(self) -> bool:
        return len(self.entries) >= MAX_ENTRIES

    def getMBB(self) -> "Box":
        """Returns the minimum bounding box for this node based on the entries."""

        boxes = [entry.box for entry in self.entries]
        return MBB(boxes)

    def insertEntry(self, entry: "Entry") -> None:
        self.entries.append(entry)

        self.assignParent()

    def parentEntry(self):
        if self.parent is not None:
            return next(entry for entry in self.parent.entries if entry.child is self)
        return None

    def assignParent(self) -> None:
        """Assign parent to child nodes"""
        if not self.isLeaf():
            for entry in self.entries:
                entry.child.parent = self

    def getLeastVolumeEnlargement(self, new_entry: "Entry") -> "Node":
        """Returns the node that will be enlarged the least after the new entry insertion"""
        enlargement_list = []
        for entry in self.entries:

            volumeEnlargement = getVolumeEnlargement(new_entry.box, entry.box)
            enlargement_list.append([entry.child, volumeEnlargement])

        # Get the Node that requires least enlargement to fit new entry.
        return min(enlargement_list, key=lambda e: e[1])[0]


class Rtree:
    def __init__(self) -> None:
        self.root = Node()

    def chooseLeaf(self, new_entry: "Entry") -> "Node":
        """Chooses a leaf node to insert the new entry based on least volume enlargement after insertion."""

        # Start from the root of the tree.
        node = self.root

        # Traverse the tree to find a suitable leaf node.
        while not node.isLeaf():
            # Get the node that requires least volume enlargement to fit the new entry.
            node = node.getLeastVolumeEnlargement(new_entry)

        return node

    def nodeSplit(self, node: "Node", new_entry: "Entry") -> "Node":
        """Splits the node using quadratic split. Changes the entry list of splitted node and returns the new node."""
        group1, group2 = quadraticSplit(node, new_entry)
        node.entries = group1
        split_node = Node(entries=group2)
        node.assignParent()
        return split_node

    def insert(self, data: "Point"):
        """This method insers a new data entry to a leaf node."""

        # Create the entry object.
        new_entry = Entry(data=data)
        leaf_node = self.chooseLeaf(new_entry)
        split_node = None
        # Split the node if necessary
        if leaf_node.isFull():
            split_node = self.nodeSplit(node=leaf_node, new_entry=new_entry)
        else:
            leaf_node.insertEntry(new_entry)
        self.adjustTree(node=leaf_node, split_node=split_node)

    def adjustTree(self, node: "Node", split_node: "Node"):
        while not node.isRoot():
            parent = node.parent
            node.parentEntry().box = node.getMBB()
            if split_node is not None:
                parent_entry = Entry(child=split_node)
                if parent.isFull():
                    self.nodeSplit(node=parent, new_entry=parent_entry)
                else:
                    parent.insertEntry(entry=parent_entry)
                    split_node = None
            node = parent
        if split_node is not None:
            self.growTree([node, split_node])

    def growTree(self, nodes):
        """Grows the R-Tree by creating a new root node, with the given nodes as children."""
        entries = [Entry(child=node) for node in nodes]
        self.root = Node(entries=entries)

    def getNodesBox(self, node):
        yield node.getMBB()
        if not node.isLeaf():
            for entry in node.entries:
                yield from self.getNodesBox(entry.child)
        else:
            for entry in node.entries:
                yield entry.getEntryBox()
    
    def query(self, t0: float, t1: float):
        """Query The tree for a specifi timeframe and retrun all data points."""
        points = []

        # Create query box.
        xmin = self.root.getMBB().x1
        xmax = self.root.getMBB().x2
        ymin = self.root.getMBB().y1
        ymax = self.root.getMBB().y2

        query_box = Box(xmin, ymin, t0, xmax, ymax, t1)
        
        boxes = [box for box in self.getNodesBox(self.root)]
        for box in boxes:
            x1, y1, z1, x2, y2, z2 = box.getCoordinates()

            if x1 == x2 and y1 == y2 and z1 == z2:
                
                # Get only overlaping boxes
                if box.overlaps(query_box):
                    points.append(box)

        return points


def MBB(boxes: "Box" = []) -> "Box":
    """Returns the minimum bounding box for all the boxes in a list."""
    x_values = []
    y_values = []
    z_values = []

    for box in boxes:
        x_values += [box.x1, box.x2]
        y_values += [box.y1, box.y2]
        z_values += [box.z1, box.z2]

    MBB = Box(
        x1=min(x_values),
        y1=min(y_values),
        z1=min(z_values),
        x2=max(x_values),
        y2=max(y_values),
        z2=max(z_values),
    )

    return MBB


def getVolumeEnlargement(new_box: "Box", old_box: "Box") -> float:
    """Returns the volume of the MBB after instering new box into old box."""
    combinedBox = MBB([new_box, old_box])
    return combinedBox.getVolume() - old_box.getVolume()


def quadraticSplit(node: "Node", new_entry: "Entry"):
    """This function implements the Quadratic Split algorithm as described in the paper."""
    # Get M+1 entries
    entry_list = node.entries
    entry_list.append(new_entry)

    # Pick the seeds for the split.
    seed1, seed2 = pickSeeds(entries=entry_list)
    entry_list.remove(seed1)
    entry_list.remove(seed2)

    # Create 2 entry groups.
    group1 = [seed1]
    group2 = [seed2]

    # Get group boinding boxes
    box1 = MBB([entry.box for entry in group1])
    box2 = MBB([entry.box for entry in group2])

    no_entries = len(entry_list)

    while no_entries > 0:
        # If one group has so few entries that all the rest must be assigned to it in order for it to meet the
        # MIN_ENTRIES requirement, assign them and stop.
        len1, len2 = (len(group1), len(group2))
        group1_underfull = len1 < MIN_ENTRIES <= len1 + no_entries
        group2_underfull = len2 < MIN_ENTRIES <= len2 + no_entries
        if group1_underfull and not group2_underfull:
            group1.extend(entry_list)
            break
        if group2_underfull and not group1_underfull:
            group2.extend(entry_list)
            break

        # Pick the next entry to assign
        vol1, vol2 = box1.getVolume(), box2.getVolume()
        entry = pickNext(entry_list, box1, vol1, box2, vol2)

        # Add it to the group whose bounding box will have to be enlarged the least to accommodate it.

        ubox1, ubox2 = MBB([box1, entry.box]), MBB([box2, entry.box])
        enlargement1 = ubox1.getVolume() - vol1
        enlargement2 = ubox2.getVolume() - vol2
        # In the case of a tie, insert to the group with the least volume, else with the least elements, else either.
        if enlargement1 == enlargement2:
            if vol1 == vol2:
                group = group1 if len1 <= len2 else group2
            else:
                group = group1 if vol1 < vol2 else group2
        else:
            group = group1 if enlargement1 < enlargement2 else group2
        group.append(entry)

        # Update groups box.
        if group is group1:
            box1 = ubox1
        else:
            box2 = ubox2
        # Remove insterted entry from the list.
        entry_list.remove(entry)
        no_entries = len(entry_list)

    return group1, group2


def pickSeeds(entries: "Entry" = []):
    """
    Returns a pair of entries (seeds) from a list, that when combined
    produce the box with the largest volume.
    """
    seeds = None
    max_volume_increase = None
    for i in range(len(entries) - 1):
        pair = entries[i : i + 2]
        entry1 = pair[0]
        entry2 = pair[1]
        volume_increase = (
            getVolumeEnlargement(entry1.box, entry2.box)
            - entry1.box.getVolume()
            - entry2.box.getVolume()
        )
        if max_volume_increase is None or volume_increase > max_volume_increase:
            max_volume_increase = volume_increase
            seeds = (entry1, entry2)

    return seeds[0], seeds[1]


def pickNext(remaining_entries, group1_box, group1_vol, group2_box, group2_vol):
    max_diff = None
    result = None
    for e in remaining_entries:
        d1 = MBB([group1_box, e.box]).getVolume() - group1_vol
        d2 = MBB([group2_box, e.box]).getVolume() - group2_vol
        diff = fabs(d1 - d2)
        if max_diff is None or diff > max_diff:
            max_diff = diff
            result = e
    return result
