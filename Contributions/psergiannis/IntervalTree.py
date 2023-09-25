from graphviz import Digraph
import random
import timeit
from memory_profiler import memory_usage


class Node:
    def __init__(self, interval, max_end):
        self.interval = interval
        self.max_end = max_end
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, node, interval):
        if node is None:
            max_end = max(interval)
            return Node(interval, max_end)

        low = interval[0]
        if low < node.interval[0]:
            node.left = self.insert(node.left, interval)
        else:
            node.right = self.insert(node.right, interval)

        if node.max_end < max(interval):
            node.max_end = max(interval)

        return node

    def delete(self, interval):
        self.root, _ = self.delete_interval(self.root, interval)

    def delete_interval(self, root, interval):
        if not root:
            return root, None

        deleted_node = None
        if root.interval == interval:
            deleted_node = root

            if root.left:
                max_node = root.left
                while max_node.right:
                    max_node = max_node.right

                root.interval = max_node.interval
                root.left, _ = self.delete_interval(root.left, max_node.interval)

            elif root.right:
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left

                root.interval = min_node.interval
                root.right, _ = self.delete_interval(root.right, min_node.interval)

            else:
                root = None

        elif interval[0] < root.interval[0]:
            root.left, deleted_node = self.delete_interval(root.left, interval)

        else:
            root.right, deleted_node = self.delete_interval(root.right, interval)

        if root:
            root.max_end = max(
                root.interval[1],
                root.left.max_end if root.left else float("-inf"),
                root.right.max_end if root.right else float("-inf"),
            )

        return root, deleted_node

    def update(self, old_interval, new_interval):
        self.delete(old_interval)
        self.root = self.insert(self.root, new_interval)

    def search(self, node, interval):
        if node is None:
            return []

        intersecting_intervals = []
        low, high = interval
        node_low, node_high = node.interval

        if node_low <= high and low <= node_high:
            intersecting_intervals.append(node.interval)

        if node.left is not None and node.left.max_end >= low:
            intersecting_intervals.extend(self.search(node.left, interval))

        if node.right is not None and node_low <= high:  # Also check the right subtree
            intersecting_intervals.extend(self.search(node.right, interval))

        return intersecting_intervals

    def build(self, intervals):
        for interval in intervals:
            self.root = self.insert(self.root, interval)


# Function to visualize the Interval Tree
def visualize_tree(node, graph=None):
    if graph is None:
        graph = Digraph()

    if node is not None:
        graph.node(f"{id(node)}", f"{node.interval}\nMax End: {node.max_end}")

        if node.left:
            graph.node(
                f"{id(node.left)}",
                f"{node.left.interval}\nMax End: {node.left.max_end}",
            )
            graph.edge(f"{id(node)}", f"{id(node.left)}", "L")
            visualize_tree(node.left, graph)

        if node.right:
            graph.node(
                f"{id(node.right)}",
                f"{node.right.interval}\nMax End: {node.right.max_end}",
            )
            graph.edge(f"{id(node)}", f"{id(node.right)}", "R")
            visualize_tree(node.right, graph)

    return graph


def demo_interval_tree():
    print("Interval Tree:")

    # Create synthetic dataset
    intervals = [(random.randint(0, 50), random.randint(51, 100)) for _ in range(20)]

    # Initialize IntervalTree and build it
    tree = IntervalTree()

    # Measure build memory usage
    mem_usage_before = memory_usage()[0]
    build_time = timeit.timeit(lambda: tree.build(intervals), number=1)
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(f"Memory used to build the tree: {max(0, mem_diff):.10f} MiB")
    print(f"Time taken to build the tree: {build_time:.10f} seconds")

    # Visualize the tree after build
    visualize_tree(tree.root).render(
        filename="interval_tree_build", view=True, format="png", cleanup=True
    )

    # Create a list of new intervals to insert
    new_intervals = [(15, 30), (32, 45), (5, 20)]

    # Measure time and memory and insert the new intervals
    for new_interval in new_intervals:
        mem_usage_before = memory_usage()[0]
        insert_time = timeit.timeit(
            lambda: tree.insert(tree.root, new_interval), number=1
        )
        mem_usage_after = memory_usage()[0]
        mem_diff = mem_usage_after - mem_usage_before
        print(
            f"Memory used to insert interval {new_interval}: {max(0, mem_diff):.10f} MiB"
        )
        print(
            f"Time taken to insert interval {new_interval}: {insert_time:.10f} seconds"
        )

    # Visualize the tree after insert
    visualize_tree(tree.root).render(
        filename="interval_tree_insert", view=True, format="png", cleanup=True
    )

    # Test deletion
    delete_interval = (32, 45)  # Modify with an actual interval from your tree
    mem_usage_before = memory_usage()[0]
    delete_time = timeit.timeit(lambda: tree.delete(delete_interval), number=1)
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(
        f"Memory used to delete interval {delete_interval}: {max(0, mem_diff):.10f} MiB"
    )
    print(f"Time taken to delete an interval: {delete_time:.10f} seconds")

    # Visualize the tree after delete
    visualize_tree(tree.root).render(
        filename="interval_tree_delete", view=True, format="png", cleanup=True
    )

    # Test update
    old_interval = (15, 30)  # Modify with an actual interval from your tree
    new_interval = (24, 100)  # Modify with the desired new interval
    mem_usage_before = memory_usage()[0]
    update_time = timeit.timeit(
        lambda: tree.update(old_interval, new_interval), number=1
    )
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(
        f"Memory used to update interval {old_interval} to {new_interval}: {max(0, mem_diff):.10f} MiB"
    )
    print(f"Time taken to update an interval: {update_time:.10f} seconds")

    # Visualize the tree after update
    visualize_tree(tree.root).render(
        filename="interval_tree_update", view=True, format="png", cleanup=True
    )

    # Test search
    search_interval = (10, 20)
    mem_usage_before = memory_usage()[0]
    search_time = timeit.timeit(
        lambda: tree.search(tree.root, search_interval), number=1
    )
    mem_usage_after = memory_usage()[0]
    mem_diff = mem_usage_after - mem_usage_before
    print(f"Memory used to search an interval: {max(0, mem_diff):.10f} MiB")
    print(f"Time taken to search an interval: {search_time:.10f} seconds")

    # Execute and print the result of the search
    found_interval = tree.search(tree.root, search_interval)
    print(f"Found interval that intersects with {search_interval}: {found_interval}")


# Call the demo function to run the code
if __name__ == "__main__":
    demo_interval_tree()
