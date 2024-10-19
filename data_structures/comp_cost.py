import random
import time

import matplotlib.pyplot as plt


# Function to measure time for list insertion.
def measure_insertion_time(num_elements):
    lst = []
    start_time = time.time()
    for i in range(num_elements):
        list.append(i)
    end_time = time.time()
    return end_time - start_time


def measure_iteration_time(coll):
    start_time = time.time()
    for k, v in coll.items():
        print(f"{k} -> {v}")
    end_time = time.time()
    return end_time - start_time


def insert_elements(num_elements):
    dict = {}
    for i in range(num_elements):
        k = ("%06x" % random.randrange(16**6)).upper()
        dict[k] = f"{i}"
    return dict


input_sizes = [10, 100, 1000, 10000, 100000]
times = []
hashmaps = []

for size in input_sizes:
    m = insert_elements(size)
    hashmaps.append(m)

for hashmap in hashmaps:
    t = measure_iteration_time(hashmap)
    times.append(t)

# Plot the results
plt.plot(input_sizes, times, marker="o")
plt.title("Time Complexity of Dictionary Iteration")
plt.xlabel("Number of Elements")
plt.ylabel("Time Taken (seconds)")
plt.show()
