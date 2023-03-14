import timeit
import random
import matplotlib.pyplot as plt


class PriorityQueue:
    def __init__(self):
        self.queue = []


    def insert(self, item, priority):
        self.queue.append((item, priority))
        self._bubble_up(len(self.queue) - 1)


    def extract_max(self):
        if len(self.queue) == 0:
            raise IndexError('Queue is empty')
        max_item = self.queue[0]
        last_item = self.queue.pop()
        if len(self.queue) > 0:
            self.queue[0] = last_item
            self._bubble_down(0)
        return max_item


    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.queue[index][1] > self.queue[parent][1]:
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
            self._bubble_up(parent)


    def _bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if left_child < len(self.queue) and self.queue[left_child][1] > self.queue[largest][1]:
            largest = left_child
        if right_child < len(self.queue) and self.queue[right_child][1] > self.queue[largest][1]:
            largest = right_child
        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self._bubble_down(largest)


def test_priority_queue(n):
    # Initialize empty priority queue
    pq = PriorityQueue()
    # Generate list of random priorities and items
    priorities = [random.randint(0, 100) for i in range(n)]
    items = list(range(n))
    random.shuffle(items)
    # Insert items into priority queue
    for i in range(n):
        pq.insert(items[i], priorities[i])
    # Extract all items from priority queue
    for i in range(n):
        pq.extract_max()


# Test inefficient implementation
n = 1000
t1 = timeit.Timer(lambda: test_priority_queue(n))
inefficient_results = t1.repeat(100, 1)


# Test efficient implementation
pq = PriorityQueue()
n = 1000
t2 = timeit.Timer(lambda: test_priority_queue(n))
efficient_results = t2.repeat(100, 1)


# Plot results
plt.hist(inefficient_results, bins=20, alpha=0.5, label='Inefficient')
plt.hist(efficient_results, bins=20, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.show()


# Print aggregate results
print('Inefficient Implementation:')
print('Min Execution Time:', min(inefficient_results))
print('Average Execution Time:', sum(inefficient_results) / len(inefficient_results))
print('Efficient Implementation:')
print('Min Execution Time:', min(efficient_results))
print('Average Execution Time:', sum(efficient_results) / len(efficient_results))
