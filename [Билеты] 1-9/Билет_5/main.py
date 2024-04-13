import matplotlib.pyplot as plt
import numpy as np

def plot_function(a, b, step):
    x = np.arange(-10, 10, step)
    y = a * np.sin(x) + b

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции y = a * sin(x) + b')
    plt.grid(True)
    plt.show()

with open('coefficients.txt', 'r') as file:
    coefficients = list(map(float, file.readline().split()))
a, b, step = coefficients
plot_function(a, b, step)
