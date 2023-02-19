class SegmentTree:
    def __init__(self, intervals):
        # Initialize the tree with the given intervals
        self.intervals = intervals
        self.tree = [None] * (4 * len(intervals))
        self.build(1, 0, len(intervals) - 1)

    def build(self, node, start, end):
    # Recursively build the segment tree
        if start == end:
            self.tree[node] = [self.intervals[start]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            self.tree[node] = []
            if self.tree[left_child] is not None:
                self.tree[node] += self.tree[left_child]
            if self.tree[right_child] is not None:
                self.tree[node] += self.tree[right_child]
            self.tree[node] = sorted(self.tree[node])

    

    def insert(self, interval):
        # Insert a new interval into the tree
        self.intervals.append(interval)
        self._insert(1, 0, len(self.intervals) - 1, len(self.intervals) - 1)

    def _insert(self, node, start, end, idx):
        # Recursively insert an interval into the tree
        if start == end:
            self.tree[node] = [self.intervals[idx]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            if len(self.tree) <= right_child:
                # Increase the size of the tree list to hold the new node
                self.tree += [None] * (right_child - len(self.tree) + 1)
            if idx <= mid:
                # Ensure that left child is initialized to an empty list if it is not yet set
                if self.tree[left_child] is None:
                    self.tree[left_child] = []
                self._insert(left_child, start, mid, idx)
            else:
                # Ensure that right child is initialized to an empty list if it is not yet set and within range
                if right_child < len(self.tree) and self.tree[right_child] is None:
                    self.tree[right_child] = []
                self._insert(right_child, mid + 1, end, idx)
            # Concatenate the sorted lists of the left and right children, checking for None values
            left_list = self.tree[left_child] if self.tree[left_child] is not None else []
            right_list = self.tree[right_child] if right_child < len(self.tree) and self.tree[right_child] is not None else []
            self.tree[node] = sorted(left_list + right_list)



    def delete(self, idx):
        # Delete an interval from the tree by index
        self.intervals.pop(idx)
        self._delete(1, 0, len(self.intervals) - 1, idx)

    def _delete(self, node, start, end, idx):
        # Recursively delete an interval from the tree
        if start == end:
            self.tree[node] = [self.intervals[start]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            if idx <= mid:
                self._delete(left_child, start, mid, idx)
            else:
                self._delete(right_child, mid + 1, end, idx)
            self.tree[node] = sorted(self.tree[left_child] + self.tree[right_child])

    def update(self, idx, new_interval):
        # Update an interval in the tree by index
        self.intervals[idx] = new_interval
        self._update(1, 0, len(self.intervals) - 1, idx)

    def _update(self, node, start, end, idx):
        # Recursively update an interval in the tree
        if start == end:
            self.tree[node] = [self.intervals[idx]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            if idx <= mid:
                self._update(left_child, start, mid, idx)
            else:
                self._update(right_child, mid + 1, end, idx)
            self.tree[node] = sorted(self.tree[left_child] + self.tree[right_child])

    def query(self, node, start, end, x):
        # Query the tree to find intervals that contain x
        if self.tree[node] is None:
            return []
        if start == end:
            return [interval for interval in self.tree[node] if interval[0] <= x <= interval[1]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            if x <= mid:
                return self.query(left_child, start, mid, x)
            else:
                return self.query(right_child, mid + 1, end, x) + self.query(left_child, start, mid, x)

    def query_point(self, x):
        # Query the tree for a point
        result = self.query(1, 0, len(self.intervals) - 1, x)
        return list(set(result))

