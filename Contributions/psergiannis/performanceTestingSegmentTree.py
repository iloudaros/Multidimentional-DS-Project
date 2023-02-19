import time
from mySegmentTree import SegmentTree

intervals = [(1, 5), (2, 9), (3, 8), (6, 10), (8, 9)]
tree = SegmentTree(intervals)

# Query the tree for a point
start_time = time.time()
result = tree.query_point(2)
end_time = time.time()
print(result)
print("Time for query:", end_time - start_time, "seconds")
print(result)  # Output: [(2, 9), (1, 5)]

# Insert a new interval into the tree
start_time = time.time()
tree.insert((7, 11))
end_time = time.time()
print(tree.intervals)  # Output: [(1, 5), (2, 9), (3, 8), (6, 10), (8, 9), (7, 11)]
print("Time for Insert:", end_time - start_time, "seconds")

# Query the tree for a point after inserting a new interval
result = tree.query_point(5)
print(result)  # Output: [(2, 9), (3, 8), (1, 5)]

# Update an interval in the tree
start_time = time.time()
tree.update(0, (2, 4))
end_time = time.time()
print("Time for Update:", end_time - start_time, "seconds")
print(tree.intervals)  # Output: [(2, 4), (2, 9), (3, 8), (6, 10), (8, 9), (7, 11)]

# Query the tree for a point after updating an interval
result = tree.query_point(3)
print(result)  # Output: [(2, 9), (3, 8), (2, 4)]

# Delete an interval from the tree
start_time = time.time()
tree.delete(2)
end_time = time.time()
print(tree.intervals)  # Output: [(2, 4), (2, 9), (6, 10), (8, 9), (7, 11)]
print("Time for Delete:", end_time - start_time, "seconds")

# Query the tree for a point after deleting an interval
result = tree.query_point(9)
print(result)  # Output: [(2, 9), (7, 11), (6, 10)]