from mySegmentTree import SegmentTree
import random
import time

# Generate 1000 intervals to insert
insert_intervals = []
for _ in range(1000):
    x = random.randint(0, 100)
    y = random.randint(x, 100)
    insert_intervals.append((x, y))

# Generate 1000 intervals to update
update_intervals = []
for _ in range(1000):
    x = random.randint(0, 100)
    y = random.randint(x, 100)
    update_intervals.append((x, y))

# Generate 1000 indices to delete
delete_indices = [random.randint(0, 999) for _ in range(1000)]

# Generate 1000 points to search
search_points = [random.randint(1, 100) for _ in range(1000)]

# Create a new SegmentTree object and time the build process
start_time = time.time()
tree = SegmentTree(insert_intervals)
end_time = time.time()
build_time = end_time - start_time
print(f"Build time: {build_time}")

# Time the insertions
start_time = time.time()
for interval in insert_intervals:
    tree.insert(interval)
end_time = time.time()
insert_time = end_time - start_time
print(f"Insert time: {insert_time}")

# Time the updates
start_time = time.time()
for i in range(1000):
    tree.update(i, update_intervals[i])
end_time = time.time()
update_time = end_time - start_time
print(f"Update time: {update_time}")

# Time the deletions
start_time = time.time()
for i in delete_indices:
    tree.delete(i)
end_time = time.time()
delete_time = end_time - start_time
print(f"Delete time: {delete_time}")

# Time the searches
start_time = time.time()
for point in search_points:
    tree.query_point(point)
end_time = time.time()
search_time = end_time - start_time
print(f"Search time: {search_time}")
