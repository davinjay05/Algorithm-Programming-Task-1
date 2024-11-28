import matplotlib.pyplot as plt
import numpy as np


def generate_data(array_size):
    x = np.arange(1, array_size + 1) 
    m = 2
    c = 5
    y = m * x + c
    return x, y


def plot_graph(graph_type, x, y):
    if graph_type == "line":
        plt.plot(x, y, marker='o', linestyle="--", color='b', label="Line Plot")
    elif graph_type == "scatter":
        plt.scatter(x, y, color='m', label="Scatter Plot")
    elif graph_type == "bar":
        plt.bar(x, y, color='c', label="Bar Plot")
    else:
        print("Invalid Input!")
        return

    plt.xlabel("X-Label")
    plt.ylabel("Y-Label")
    plt.title(f"{graph_type.capitalize()} Graph with {len(x)} points.")
    plt.legend()

    plt.show()


print("Enter the graph type: line, scatter, or bar")
graph_type = input("Choose graph type: ").strip().lower()

try:
    array_size = int(input("Enter the size of the array you want (10-10000): ").strip())
    if 10 <= array_size <= 10000:
        x, y = generate_data(array_size)
        plot_graph(graph_type, x, y)
    else:
        print("Please enter a size between 10 and 10000!")
except ValueError:
    print("Invalid Input! Please enter the size of the array!")
