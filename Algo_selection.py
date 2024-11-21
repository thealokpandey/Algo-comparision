import time
import random
import matplotlib.pyplot as plt

# Implementation of SelectionSort
def selectionSort(array, length):
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

# A posteriori analysis of QuickSort
def measure_execution_time(array_sizes):
    execution_times = []
    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time_ns()
        length =len(arr)
        selectionSort(arr,length)
        end_time = time.time_ns()
        execution_times.append(end_time - start_time)
    return execution_times

# Define input sizes for analysis
input_sizes = [100, 500, 1000, 5000, 10000, 20000]

# Measure execution times
execution_times = measure_execution_time(input_sizes)

# Plot results for a posteriori analysis
def plot_graph_6():
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x**2 for x in input_sizes], linestyle='--', color='red', label="Theoretical O(n^2)")
    plt.xlabel("Input Size (Number of Elements)")
    plt.ylabel("Execution Time (NanoSeconds)")
    plt.title("A Posteriori vs A Priori Analysis of Selection Sort O(n^2)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.show()
def compare_graph_a3():
    plt.subplot(2,2,3)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x**2 for x in input_sizes], linestyle='--', color='red', label="Theoretical O(n^2)")
    plt.title(" Selection Sort O(n^2)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis

def compare_graph_3():
    plt.subplot(2,3,5)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x**2 for x in input_sizes], linestyle='--', color='red', label="Theoretical O(n^2)")
    plt.title("O(n^2)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis


if __name__ == "__main__":
    plot_graph_6()