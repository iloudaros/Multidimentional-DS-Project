import time
from myIntervalTree import IntervalTree
tree = IntervalTree()

# Insert intervals
tree.insert(1, 5)
tree.insert(2, 9)
tree.insert(3, 8)
tree.insert(6, 10)
start_time = time.time()
tree.insert(8, 9)
end_time = time.time()
print("Time for Insert:", end_time - start_time, "seconds")
print('Nodes after Insert:')
tree.print_nodes()


# Delete an interval
start_time = time.time()
tree.delete(2, 9)
end_time = time.time()
print("Time for Delete:", end_time - start_time, "seconds")
print('Nodes after Delete:')
tree.print_nodes()

# Update an interval
start_time = time.time()
tree.update(3, 8, 10, 15)
end_time = time.time()
print("Time for Update:", end_time - start_time, "seconds")
print('Nodes after Update:')
tree.print_nodes()

# Search for an interval
start_time = time.time()
result = tree.search(8, 9)
end_time = time.time()
print("Time for Search:", end_time - start_time, "seconds")
print(f'First intersection: {result}') 
