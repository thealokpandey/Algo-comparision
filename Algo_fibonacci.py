import time
import matplotlib.pyplot as plt
import numpy as np
import random

def recursive_fibonacci(n):
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

recursive_fibonacci(6)

def measure_execution_time(n):
    start_time = time.time_ns()
    recursive_fibonacci(n)
    end_time = time.time_ns()
    return end_time - start_time

# Generate input sizes
random_numbers = range(1, 30)
# random_numbers = [random.choice(input_sizes) for _ in range(15)]  # Generate 10 random numbers
# random_numbers.sort()
# print(random_numbers)
# Measure execution times
execution_times = []
for n in random_numbers:
    execution_time = measure_execution_time(n)
    execution_times.append(execution_time)

# Theoretical time complexity: O(2^n)
theoretical_times = [2**n * 10 for n in random_numbers]  # Adjust the constant factor as needed

# Plot the results
def plot_graph_7():
    plt.plot(random_numbers, execution_times, label="Measured Execution Time")
    plt.plot(random_numbers, theoretical_times, label="Theoretical O(2^n)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("Recursive Fibonacci: Measured vs. Theoretical Execution Time O(2^n)")
    plt.legend()
    plt.grid(True)
    plt.show()

def compare_graph_8():
    plt.subplot(2,3,6)
    plt.plot(random_numbers, execution_times, label="Measured Execution Time")
    plt.plot(random_numbers, theoretical_times, label="Theoretical O(2^n)")
    plt.title("O(2^n)")
    plt.legend()
    plt.grid(True)

if __name__ == "__main__":
    plot_graph_7()