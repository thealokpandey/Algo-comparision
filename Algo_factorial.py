import time
import matplotlib.pyplot as plt
import numpy as np

def factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def measure_execution_time(n, num_trials=10):
    total_time = 0
    for _ in range(num_trials):
        start_time = time.perf_counter_ns()
        factorial(n)
        end_time = time.perf_counter_ns()
        total_time += end_time - start_time
    return total_time / num_trials

# Generate input sizes
input_sizes = range(1,100 )

# Measure execution times
execution_times = []
for n in input_sizes:
    execution_time = measure_execution_time(n)
    execution_times.append(execution_time)

# Theoretical time complexity: O(n)
theoretical_times = [n * 100 for n in input_sizes]  # Adjust the constant factor as needed

# Plot the results
def plot_graph_2():
    plt.plot(input_sizes, execution_times, label="Measured Execution Time")
    plt.plot(input_sizes, theoretical_times, label="Theoretical O(n)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("Factorial Function: Measured vs. Theoretical Execution Time O(n)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.show()

def compare_graph_6():
    plt.subplot(2,3,2)
    plt.plot(input_sizes, execution_times, label="Measured Execution Time")
    plt.plot(input_sizes, theoretical_times, label="Theoretical O(n)")
    plt.title("O(n)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')


if __name__ == "__main__":
    plot_graph_2()