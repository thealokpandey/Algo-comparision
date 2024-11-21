import time
import random
import matplotlib.pyplot as plt

# Implementation of QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# A posteriori analysis of QuickSort
def measure_execution_time(array_sizes):
    execution_times = []
    
    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        execution_times.append(end_time - start_time)
    
    return execution_times

# Define input sizes for analysis
input_sizes = [100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 100000]

# Measure execution times
execution_times = measure_execution_time(input_sizes)

# Plot results for a posteriori analysis
def plot_graph_5():
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='--', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.xlabel("Input Size (Number of Elements)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("A Posteriori vs A Priori Analysis of Quick Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.show()
def compare_graph_a2():
    plt.subplot(2,2,2)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='--', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.title("Quick Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    
if __name__ == "__main__":
    plot_graph_5()