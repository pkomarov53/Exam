import matplotlib.pyplot as plt
import numpy as np

def plot_function(a, b, c, step):
    x = np.arange(-1, 1, step)
    y = a / (b * x + c)

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции y = a / (b * x + c)')
    plt.grid(True)
    plt.show()

with open('coefficients.txt', 'r') as file:
    coefficients = list(map(float, file.readline().split()))
a, b, c, step = coefficients
plot_function(a, b, c, step)
