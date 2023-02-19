

from myIntervalTree import IntervalTree
import time
import sys
sys.setrecursionlimit(10000)  # Set the maximum recursion depth to 10000

start = time.time()
tree = IntervalTree()
end = time.time()
print(f"Time taken to build: {end - start} seconds")

# Measure the performance of the insert operation for intervals of size 1000
for size in [1000]:
    total_time = 0
    num_runs = 10
    for i in range(num_runs):
        start = time.time()
        for j in range(size):
            tree.insert(j, j + 10)
        end = time.time()
        total_time += end - start
    average_time = total_time / num_runs
    print(f"Average time taken to insert {size} intervals: {average_time} seconds")

# Measure the performance of the update operation for intervals of size 1000
for size in [1000]:
    total_time = 0
    num_runs = 10
    for i in range(num_runs):
        for j in range(size):
            tree.insert(j, j + 10)
        start = time.time()
        for j in range(size):
            tree.update(j, j + 10, j + 1, j + 11)
        end = time.time()
        total_time += end - start
    average_time = total_time / num_runs
    print(f"Average time taken to update {size} intervals: {average_time} seconds")

# Measure the performance of the delete operation for intervals of size 1000
for size in [1000]:
    total_time = 0
    num_runs = 10
    for i in range(num_runs):
        for j in range(size):
            tree.insert(j, j + 10)
        start = time.time()
        for j in range(size):
            tree.delete(j, j + 10)
        end = time.time()
        total_time += end - start
    average_time = total_time / num_runs
    print(f"Average time taken to delete {size} intervals: {average_time} seconds")


# Measure the performance of the search operation for intervals of size 1000
for size in [1000]:
    total_time = 0
    num_runs = 10
    for i in range(num_runs):
        for j in range(size):
            tree.insert(j, j + 10)
        start = time.time()
        for j in range(size):
            tree.search(j, j + 10)
        end = time.time()
        total_time += end - start
    average_time = total_time / num_runs
    print("Average time for searching an interval: {:.10f} seconds".format(average_time))
