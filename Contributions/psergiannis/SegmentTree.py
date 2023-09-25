import random
import timeit
from graphviz import Digraph
from memory_profiler import memory_usage


class SegmentTree:
    def __init__(self, size, arr=None):
        self.size = size
        self.arr = arr if arr else [0] * size  # Keep the original array if it exists
        self.tree = [0] * (4 * size)
        if self.arr:
            self.build(self.arr, 1, 0, self.size - 1)

    def build(self, arr, i, l, r):
        if l == r:
            self.tree[i] = arr[l]
            return
        mid = (l + r) // 2
        self.build(arr, 2 * i, l, mid)
        self.build(arr, 2 * i + 1, mid + 1, r)
        self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def insert(self, val):
        # If the original array exists, append the value to it and rebuild the tree
        if self.arr:
            self.arr.append(val)
            self.size += 1
            self.tree = [0] * (4 * self.size)
            self.build(self.arr, 1, 0, self.size - 1)

    def delete(self, idx):
        if 0 <= idx < self.size and self.arr:
            self.arr.pop(idx)  # Remove the element at idx from arr
            self.size -= 1  # Reduce the size of the Segment Tree
            self.tree = [0] * (4 * self.size)  # Adjust the size of the tree list
            self.build(self.arr, 1, 0, self.size - 1)  # Rebuild the tree

    def update(self, i, val, idx, l, r):
        if l == r:
            self.tree[i] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * i, val, idx, l, mid)
        else:
            self.update(2 * i + 1, val, idx, mid + 1, r)
        self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def stabbing_query(self, idx):
        """
        Returns the value at idx in the original array.
        """
        if 0 <= idx < self.size:
            return self._stabbing_query(1, 0, self.size - 1, idx)
        else:
            raise IndexError("Index out of range")

    def _stabbing_query(self, i, l, r, idx):
        if l == r:
            return self.tree[i]
        mid = (l + r) // 2
        if idx <= mid:
            return self._stabbing_query(2 * i, l, mid, idx)
        else:
            return self._stabbing_query(2 * i + 1, mid + 1, r, idx)

    def range_query(self, ql, qr):
        """
        Returns the sum of elements in the original array in the range [ql, qr].
        """
        if 0 <= ql <= qr < self.size:
            return self._range_query(1, 0, self.size - 1, ql, qr)
        else:
            raise IndexError("Query range out of bounds")

    def _range_query(self, i, l, r, ql, qr):
        if ql <= l and r <= qr:  # If the current segment is within the query range
            return self.tree[i]
        if qr < l or r < ql:  # If the current segment is outside the query range
            return 0
        mid = (l + r) // 2
        # If the current segment overlaps with the query range,
        # compute the sum of the left and right children.
        return self._range_query(2 * i, l, mid, ql, qr) + self._range_query(
            2 * i + 1, mid + 1, r, ql, qr
        )

    def visualize_tree(self):
        dot = Digraph(comment="Segment Tree")
        self._visualize_tree(1, 0, self.size - 1, dot)
        return dot

    def _visualize_tree(self, i, l, r, dot):
        dot.node(f"{i}", label=f"{self.tree[i]}\n[{l}-{r}]")  # Updated line
        if l == r:
            return
        mid = (l + r) // 2
        left_child_idx = 2 * i
        right_child_idx = 2 * i + 1
        self._visualize_tree(left_child_idx, l, mid, dot)
        self._visualize_tree(right_child_idx, mid + 1, r, dot)
        dot.edge(f"{i}", f"{left_child_idx}")
        dot.edge(f"{i}", f"{right_child_idx}")


def demo_segment_tree():
    print("Segment Tree:")

    # Create synthetic dataset
    n = 20
    arr = [random.randint(1, 100) for _ in range(n)]

    # Initialize SegmentTree and build it
    seg_tree = SegmentTree(n, arr)

    # Measure build memory usage
    mem_usage_before = memory_usage()[0]
    build_time = timeit.timeit(lambda: seg_tree.build(arr, 1, 0, n - 1), number=1)
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(f"Memory used to build the tree: {max(0, mem_diff):.10f} MiB")
    print(f"Time taken to build the tree: {build_time:.10f} seconds")

    # Visualize the tree
    dot = seg_tree.visualize_tree()
    dot.render("segment_tree_build", view=True, format="png", cleanup=True)

    # Measure insert memory usage and time
    mem_usage_before = memory_usage()[0]
    insert_time = timeit.timeit(lambda: seg_tree.insert(50), number=1)
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(f"Memory used to insert an element: {max(0, mem_diff):.10f} MiB")
    print(f"Time taken to insert an element: {insert_time:.10f} seconds")
    dot = seg_tree.visualize_tree()
    dot.render("segment_tree_insert", view=True, format="png", cleanup=True)

    # Measure delete memory usage and time (Ensure index 2 exists in the tree)
    if 2 < seg_tree.size:
        mem_usage_before = memory_usage()[0]
        delete_time = timeit.timeit(lambda: seg_tree.delete(2), number=1)
        mem_usage_after = memory_usage()[0]
        mem_diff = mem_usage_after - mem_usage_before
        print(f"Memory used to delete an element: {max(0, mem_diff):.10f} MiB")
        print(f"Time taken to delete an element: {delete_time:.10f} seconds")
        dot = seg_tree.visualize_tree()
        dot.render("segment_tree_delete", view=True, format="png", cleanup=True)

    # Measure update memory usage and time (Ensure index 2 exists in the tree)
    if 2 < seg_tree.size:
        mem_usage_before = memory_usage()[0]
        update_time = timeit.timeit(
            lambda: seg_tree.update(1, 55, 2, 0, n - 1), number=1
        )
        mem_usage_after = memory_usage()[0]
        mem_diff = mem_usage_after - mem_usage_before
        print(f"Memory used to update an element: {max(0, mem_diff):.10f} MiB")
        print(f"Time taken to update an element: {update_time:.10f} seconds")
        dot = seg_tree.visualize_tree()
        dot.render("segment_tree_update", view=True, format="png", cleanup=True)

    # Measure stabbing_query memory usage and time (Ensure index 2 exists in the tree)
    if 2 < seg_tree.size:
        mem_usage_before = memory_usage()[0]
        stabbing_query_time = timeit.timeit(
            lambda: seg_tree.stabbing_query(2), number=1
        )
        mem_usage_after = memory_usage()[0]
        mem_diff = mem_usage_after - mem_usage_before
        print(f"Memory used to perform a stabbing query: {max(0, mem_diff):.10f} MiB")
        print(
            f"Time taken to perform a stabbing query: {stabbing_query_time:.10f} seconds"
        )

    # Results
    stabbing_query_result = seg_tree.stabbing_query(11)
    print(f"Stabbing query result for index 11: {stabbing_query_result}")

    # Define a tuple variable holding the range
    query_range = (2, 10)

    # Measure range_query memory usage and time (Ensure the defined range exists in the tree)
    ql, qr = query_range
    if ql < seg_tree.size and qr < seg_tree.size:
        mem_usage_before = memory_usage()[0]
        range_query_time = timeit.timeit(lambda: seg_tree.range_query(ql, qr), number=1)
        mem_usage_after = memory_usage()[0]
        mem_diff = mem_usage_after - mem_usage_before
        print(f"Memory used to perform a range query: {max(0, mem_diff):.10f} MiB")
        print(f"Time taken to perform a range query: {range_query_time:.10f} seconds")
        range_query_result = seg_tree.range_query(ql, qr)
        print(
            f"Range query result for sum in range {query_range}: {range_query_result}"
        )


# Call the demo_segment_tree function to run the code
if __name__ == "__main__":
    demo_segment_tree()
