import matplotlib.pyplot as plt


from Algo_O_1 import plot_graph_1,compare_graph_5
from Algo_factorial import plot_graph_2,compare_graph_6
from Algo_Binary import plot_graph_3,compare_graph_7
from Algo_heap import plot_graph_4,compare_graph_a1,compare_graph_1
from Algo_quick import plot_graph_5,compare_graph_a2
from Algo_selection import plot_graph_6,compare_graph_a3,compare_graph_3
from Algo_fibonacci import plot_graph_7,compare_graph_8
from Algo_merge import plot_graph_8,compare_graph_a4
 
while True:
    print('''Select a graph:
    1.O(1) Linear Search
    2.O(n) Factorial
    3.O(logn) Binary Search
    4.O(nlogn) Heap Sort
    5.O(nlogn) Quick Sort
    6.O(n^2) Selection Sort
    7.O(2^n) Fibonacci
    8.O(nlogn) Merge Sort
    9.Compare between Sorting Algorithm
    10.Compare between all time complexity
    11.Exit''')
    n=int(input("Enter a choice between 1 to 11:"))
    
    if n==1:
        plot_graph_1()
    elif n==2:
        plot_graph_2()
    elif n==3:
        plot_graph_3()
    elif n==4:
        plot_graph_4()
    elif n==5:
        plot_graph_5()
    elif n==6:
        plot_graph_6()
    elif n==7:
        plot_graph_7()
    elif n==8:
        plot_graph_8()
    elif n==9:
        compare_graph_a1()
        compare_graph_a2()
        compare_graph_a3()
        compare_graph_a4()
        plt.suptitle("Sorting Algorithm")
        plt.show()
    elif n==10:
        compare_graph_5()
        compare_graph_6()
        compare_graph_7()
        compare_graph_1()
        compare_graph_3()
        compare_graph_8()
        plt.suptitle("Time Complexity")
        plt.show() 
    elif n==11:
        break   
    else:
        print("Enter a valid choice")

