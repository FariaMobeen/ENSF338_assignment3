# Insertion in and extraction from priority queue


import timeit
import random
import statistics
import matplotlib.pyplot as plt
import heapq
from queue import PriorityQueue


# code for an inefficient implementation
class PriorityQueueList:
   def __init__(self):
       self.queue = []


   def insert(self, priority, item):
       self.queue.append((priority, item))
       self.queue = sorted(self.queue, key=lambda x: x[0])


   def pop(self):
       if len(self.queue) == 0:
           return None
       item = self.queue[0]
       self.queue = self.queue[1:]
       return item
# Worst-case complexity: O(nlogn)


# efficient implementation
class PriorityQueueHeap:
   def __init__(self):
       self.queue = []


   def insert(self, priority, item):
       heapq.heappush(self.queue, (priority, item))


   def pop(self):
       if len(self.queue) == 0:
           return None
       item = heapq.heappop(self.queue)
       return item


# provide the code for an experiment that demonstrates the difference.
n = 1000
trials = 100


# Generate random data
data = [random.randint(0, 1000000) for i in range(n)]


# Measure time for inefficient priority queue
inefficient_times = []
for i in range(trials):
   pq = PriorityQueueList()
   start_time = timeit.default_timer()
   for item in data:
       pq.insert(item)
   while not pq.is_empty():
       pq.extract_min()
   end_time = timeit.default_timer()
   inefficient_times.append(end_time - start_time)


# Measure time for efficient priority queue
efficient_times = []
for i in range(trials):
   pq = PriorityQueueHeap()
   start_time = timeit.default_timer()
   for item in data:
       pq.insert(item)
   while not pq.is_empty():
       pq.extract_min()
   end_time = timeit.default_timer()
   efficient_times.append(end_time - start_time)


# Print aggregate times
print("Inefficient: min={}, avg={}".format(min(inefficient_times), statistics.mean(inefficient_times)))
print("Efficient: min={}, avg={}".format(min(efficient_times), statistics.mean(efficient_times)))


# Plot time distributions
plt.hist(inefficient_times, bins=20, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, bins=20, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.show()
