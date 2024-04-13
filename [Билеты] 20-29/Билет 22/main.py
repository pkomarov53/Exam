import matplotlib.pyplot as plt
import numpy as np


def plot_function(a, b, c, step):
    x = np.arange(0, 1, step)
    y = a * np.tan(b * x) + c

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции y = {} * tan({} * x) + {}'.format(a, b, c))
    plt.grid(True)
    plt.show()


def main():
    with open('coefficients.txt', 'r') as file:
        coefficients = file.readline().strip().split()
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])
    step = float(coefficients[3])

    plot_function(a, b, c, step)


if __name__ == "__main__":
    main()
