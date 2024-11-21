import time
import matplotlib.pyplot as plt
import numpy as np

def first_element(array):
  return array[0]

def measure_execution_time(array_size):
  array = [i for i in range(array_size)]
  start_time = time.time_ns()
  first_element(array)
  end_time = time.time_ns()
  return end_time - start_time

# Generate input sizes
input_sizes = range(1, 1000, 10)

# Measure execution times
execution_times = []
for n in input_sizes:
    execution_time = measure_execution_time(n)
    execution_times.append(execution_time)

# Theoretical execution time (constant)
theoretical_times = [100] * len(input_sizes)  # Adjust the constant value as needed

# Plot the results
def plot_graph_1():
   plt.plot(input_sizes, execution_times, label="Measured Execution Time")
   plt.plot(input_sizes, theoretical_times, label="Theoretical Constant Time")
   plt.xlabel("Input Size (n)")
   plt.ylabel("Execution Time (Nanoseconds)")
   plt.title("First Element Function: Measured vs. Theoretical Execution Time O(1)")
   plt.legend()
   plt.grid(True)
   plt.show()

def compare_graph_5():
   plt.subplot(2,3,1)
   plt.plot(input_sizes, execution_times, label="Measured Execution Time")
   plt.plot(input_sizes, theoretical_times, label="Theoretical Constant Time")
   plt.title("O(1)")
   plt.legend()
   plt.grid(True)
   
if __name__ == "__main__":
   plot_graph_1()