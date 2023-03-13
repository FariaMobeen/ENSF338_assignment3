#code from chatgpt
# Search in a sorted array
import random
import time
import numpy as np
import matplotlib.pyplot as plt
# code for an inefficient implementation
def linear_search(arr, x):
   for i in range(len(arr)):
       if arr[i] == x:
           return i
   return -1
# efficient implementation
def binary_search(arr, x):
   low = 0
   high = len(arr) - 1
   while low <= high:
       mid = (low + high) // 2
       if arr[mid] == x:
           return mid
       elif arr[mid] < x:
           low = mid + 1
       else:
           high = mid - 1
   return -1


# State the worst-case complexity of each
# Linear Search: O(n)
# Binary Search: O(log n)


# provide the code for an experiment that demonstrates the difference.
def linear_search(arr, x):
   for i in range(len(arr)):
       if arr[i] == x:
           return i
   return -1


def binary_search(arr, x):
   low = 0
   high = len(arr) - 1
   while low <= high:
       mid = (low + high) // 2
       if arr[mid] == x:
           return mid
       elif arr[mid] < x:
           low = mid + 1
       else:
           high = mid - 1
   return -1


# Generate a sorted array of size n
n = 1000
arr = sorted([random.randint(0, n) for i in range(n)])


# Search for a random element in the array and time both search methods
x = random.randint(0, n)
linear_search_times = []
binary_search_times = []
for i in range(100):
   start = time.time()
   linear_search(arr, x)
   end = time.time()
   linear_search_times.append(end - start)


   start = time.time()
   binary_search(arr, x)
   end = time.time()
   binary_search_times.append(end - start)


# Plot the distribution of measured values across multiple measurements
plt.hist(linear_search_times, bins=20, alpha=0.5, label='Linear Search')
plt.hist(binary_search_times, bins=20, alpha=0.5, label='Binary Search')
plt.legend(loc='upper right')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.title('Search in a Sorted Array')
plt.show()


# Print an aggregate of the measured values
print('Linear Search Min Time: ', np.min(linear_search_times))
print('Binary Search Min Time: ', np.min(binary_search_times))

