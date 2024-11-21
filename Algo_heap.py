import time
import random
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child of root exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap them and recursively heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

def measure_execution_time(array_sizes):
    execution_times = []
    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time_ns()
        heap_sort(arr)
        end_time = time.time_ns()
        execution_times.append(end_time - start_time)
    return execution_times

# Define input sizes for analysis
input_sizes = [100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 100000]

# Measure execution times
execution_times = measure_execution_time(input_sizes)

# Plot results for a posteriori analysis
def plot_graph_4():
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='--', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.xlabel("Input Size (Number of Elements)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("A Posteriori vs A Priori Analysis of Heap Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.show()

def compare_graph_a1():
    plt.subplot(2,2,1)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='-', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.title("Heap Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis

def compare_graph_1():
    plt.subplot(2,3,4)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='-', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.title("O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    
if __name__ == "__main__":
    plot_graph_4()