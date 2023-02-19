class IntervalTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = high
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, low, high):
        self.root = self._insert(self.root, low, high)

    def _insert(self, node, low, high):
        if not node:
            return IntervalTreeNode(low, high)
        if low < node.low:
            node.left = self._insert(node.left, low, high)
        else:
            node.right = self._insert(node.right, low, high)
        node.max = max(node.max, high)
        return node

    def delete(self, low, high):
        self.root = self._delete(self.root, low, high)

    def _delete(self, node, low, high):
        if not node:
            return None
        if low == node.low and high == node.high:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_node = self._find_min(node.right)
            node.low = min_node.low
            node.high = min_node.high
            node.right = self._delete(node.right, min_node.low, min_node.high)
        elif low < node.low:
            node.left = self._delete(node.left, low, high)
        else:
            node.right = self._delete(node.right, low, high)
        node.max = max(node.high, self._max(node.left), self._max(node.right))
        return node

    def search(self, low, high):
        return self._search(self.root, low, high)

    def _search(self, node, low, high):
        if not node:
            return None
        if node.low <= high and low <= node.high:
            return (node.low, node.high)
        if node.left and node.left.max >= low:
            return self._search(node.left, low, high)
        return self._search(node.right, low, high)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def _max(self, node):
        return node.max if node else -float('inf')

    def update(self, low, high, new_low, new_high):
        self.delete(low, high)
        self.insert(new_low, new_high)

    def print_nodes(self):
        self._print_nodes(self.root)

    def _print_nodes(self, node):
        if node:
            self._print_nodes(node.left)
            print(f'[{node.low}, {node.high}]')
            self._print_nodes(node.right)


