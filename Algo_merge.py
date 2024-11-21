import matplotlib.pyplot as plt
import time
import random

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    merge_sort(arr, 0, len(arr) - 1)

    
def measure_time(arr):
    start_time = time.time()
    merge_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Generate input arrays of different sizes
input_sizes = [10, 100, 1000, 10000, 100000]
execution_times = []

for size in input_sizes:
    arr = [random.randint(1, 100) for _ in range(size)]
    time_taken = measure_time(arr)
    execution_times.append(time_taken)


# Plot results for a posteriori analysis
def plot_graph_8():
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='--', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.xlabel("Input Size (Number of Elements)")
    plt.ylabel("Execution Time (Nanoseconds)")
    plt.title("A Posteriori vs A Priori Analysis of Merge Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis
    plt.show()
def compare_graph_a4():
    plt.subplot(2,2,4)
    plt.plot(input_sizes, execution_times, marker='o', label="Measured Execution Time")
    plt.plot(input_sizes, [x * (x.bit_length() - 1) for x in input_sizes], linestyle='--', color='red', label="A Priori (Theoretical) O(n log n)")
    plt.title("Merge Sort O(nlogn)")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Logarithmic scale for y-axis

if __name__ == "__main__":
    plot_graph_8()