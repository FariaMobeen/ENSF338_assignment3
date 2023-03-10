

import json
import time
import matplotlib.pyplot as plt


def binary_search(arr, x, start_mid=0):
   """Search for the element x in the sorted array arr."""
   low = 0
   high = len(arr) - 1
   mid = start_mid
  
   while low <= high:
       if arr[mid] < x:
           low = mid + 1
       elif arr[mid] > x:
           high = mid - 1
       else:
           return mid
      
       mid = (low + high) // 2
  
   return -1




def time_binary_search(array, task):
   """Time the performance of binary search with different midpoints for a single task."""
   num_iterations = 5
   best_time = float('inf')
   best_midpoint = -1
  
   for i in range(num_iterations):
       # Try different midpoints
       for midpoint in range(len(array)):
           start_time = time.time()
           binary_search(array, task, start_mid=midpoint)
           end_time = time.time()
          
           search_time = end_time - start_time
           if search_time < best_time:
               best_time = search_time
               best_midpoint = midpoint
  
   return best_midpoint




# Load ex2data.json and ex2tasks.json
try:
   with open('ex2data.json') as f:
       array = json.load(f)
except FileNotFoundError:
   print("Error: ex2data.json not found.")
   exit()


try:
   with open('ex2tasks.json') as f:
       tasks = json.load(f)
except FileNotFoundError:
   print("Error: ex2tasks.json not found.")
   exit()


# Choose the best midpoint for each task
best_midpoints = {}
for task in tasks:
   best_midpoint = time_binary_search(array, task)
   best_midpoints[task] = best_midpoint
   print(f"Best midpoint for {task}: {best_midpoint}")


# Produce scatterplot
plt.scatter(tasks, [best_midpoints[task] for task in tasks])
plt.title("Best Midpoint for Binary Search Tasks")
plt.xlabel("Task")
plt.ylabel("Best Midpoint")
plt.show()


# Perform binary search on each task with the best midpoint
for task in tasks:
   index = binary_search(array, task, start_mid=best_midpoints[task])
  
   if index == -1:
       print(f"{task} not found in array")
   else:
       print(f"{task} found at index {index}")


