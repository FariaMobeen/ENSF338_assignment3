#code from chatgpt
import json
import time
from urllib.request import urlopen
import matplotlib.pyplot as plt




def binary_search(arr, x, start_mid):
   """Search for the element x in the sorted array arr using binary search."""
   low = 0
   high = len(arr) - 1
   mid = start_mid
 
   # Continue searching while the search range is not empty
   while low <= high:
       if arr[mid] < x:
           low = mid + 1
       elif arr[mid] > x:
           high = mid - 1
       else:
           # x is found at index mid
           return mid
     
       # Narrow down the search range
       mid = (low + high) // 2
 
   # x is not found in arr
   return -1




import random


def time_binary_search(array, task):
   """Time the performance of binary search with different midpoints for a single task."""
   num_iterations = 5
   best_time = float('inf')
   best_midpoint = -1
 
   for i in range(num_iterations):
       
       midpoint = 0
       start_time = time.time()
       binary_search(array, task, start_mid=midpoint)
       end_time = time.time()
         
       search_time = end_time - start_time
       if search_time < best_time:
           best_time = search_time
           best_midpoint = midpoint
 
   return best_midpoint




# Load ex2data.json and ex2tasks.json from URLs
try:
    with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json') as f:
        array = json.load(f)
except:
    print("Error: Could not load ex2data.json from URL.")
    exit()




try:
    with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json') as f:
        tasks = json.load(f)
except:
    print("Error: Could not load ex2tasks.json from URL.")
    exit()


# Choose the best midpoint for each task
best_midpoints = {}
for task in tasks:


   best_midpoint = time_binary_search(array, task)
   best_midpoints[task] = best_midpoint


# Perform binary search on each task with the best midpoint found
   start_time = time.time()
   index = binary_search(array, task, start_mid=best_midpoints[task])
   end_time = time.time()
   if index == -1:
       print(f"{task} not found in array")
   else:
        print(f"Best midpoint for {task}: {best_midpoints[task]}. {task} found at index {index}. Time taken: {end_time - start_time} seconds")


# Produce scatterplot of tasks vs best midpoints found
plt.scatter(tasks, [best_midpoints[task] for task in tasks])
plt.title("Best Midpoint for Binary Search Tasks")
plt.xlabel("Task")
plt.ylabel("Best Midpoint")
plt.show()



