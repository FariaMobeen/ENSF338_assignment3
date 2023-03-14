#code from chatgpt
import sys


prev_capacity = sys.getsizeof([])


for i in range(64):
   list = list(range(i))
   curr_capacity = sys.getsizeof(lst)


   if curr_capacity != prev_capacity:
       print(f"Capacity changed from {prev_capacity} bytes to {curr_capacity} bytes for list of length {i}.")


   prev_capacity = curr_capacity


