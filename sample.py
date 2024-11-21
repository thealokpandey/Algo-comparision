
import time
import matplotlib.pyplot as plt
import numpy as np
import random

# Recursive Fibonacci function
def recursive_fibonacci(n):
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Measure execution time (multiple runs for more accuracy)
def measure_execution_time(n, runs=10):
    total_time = 0
    for _ in range(runs):
        start_time = time.perf_counter()  # Use perf_counter for better precision
        recursive_fibonacci(n)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / runs  # Average time over multiple runs

# Generate input sizes
input_sizes = range(10, 40)
random_numbers = [random.choice(input_sizes) for _ in range(10)]  # Generate 10 random numbers
random_numbers.sort()

print("Random numbers:", random_numbers)

# Measure execution times for each random number
execution_times = []
for n in random_numbers:
    execution_time = measure_execution_time(n)
    execution_times.append(execution_time)

# Theoretical time complexity: O(2^n)
theoretical_times = [2**n * 10 for n in random_numbers]  # Adjust the constant factor as needed

# Plot the results
def plot_graph_7():
    plt.plot(random_numbers, execution_times, label="Measured Execution Time", marker='o')
    plt.plot(random_numbers, theoretical_times, label="Theoretical O(2^n)", linestyle='--')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (Seconds)")
    plt.title("Recursive Fibonacci: Measured vs. Theoretical Execution Time O(2^n)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Compare graph with subplot
def compare_graph_8():
    plt.subplot(2, 3, 6)
    plt.plot(random_numbers, execution_times, label="Measured Execution Time", marker='o')
    plt.plot(random_numbers, theoretical_times, label="Theoretical O(2^n)", linestyle='--')
    plt.title("O(2^n)")
    plt.legend()
    plt.grid(True)

if __name__ == "__main__":
    plot_graph_7()
