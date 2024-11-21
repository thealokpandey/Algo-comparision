import time
import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1
def measure_execution_time(n, target, num_trials=10):
    total_time = 0
    for _ in range(num_trials):
        arr = sorted(np.random.randint(1, 10000, n))  # Increase input size
        start_time = time.perf_counter_ns()
        binary_search(arr, target)
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time
    return total_time / num_trials

# Generate input sizes
input_sizes = [2**i for i in range(15)]  # Increase input size range

# Measure execution times
execution_times = []
for n in input_sizes:
    execution_time = measure_execution_time(n, target=5000)  # Increase target value
    execution_times.append(execution_time)

# Theoretical time complexity: O(log n)
theoretical_times = [np.log2(n) * 100 for n in input_sizes]  # Adjust the constant factor as needed

# Plot the results
def plot_graph_3():
    plt.plot(input_sizes, execution_times, label="Measured Execution Time")
    plt.plot(input_sizes, theoretical_times, label="Theoretical O(log n)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("Binary Search: Measured vs. Theoretical Execution Time O(logn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.show()

def compare_graph_7():
   plt.subplot(2,3,3)
   plt.plot(input_sizes, execution_times, label="Measured Execution Time")
   plt.plot(input_sizes, theoretical_times, label="Theoretical O(log n)")
   plt.title("O(logn)")
   plt.legend()
   plt.grid(True)
   plt.yscale('log')

if __name__ == "__main__":
    plot_graph_3()