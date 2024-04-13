import matplotlib.pyplot as plt
import numpy as np


def plot_function(a, b, step):
    x = np.arange(0, 1, step)
    y = a ** (3 * x) + b

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph of y = {}^3x + {}'.format(a, b))
    plt.grid(True)
    plt.show()


def main():
    with open('coefficients.txt', 'r') as file:
        coefficients = file.readline().strip().split()
    a = float(coefficients[0])
    b = float(coefficients[1])
    step = float(coefficients[2])
    print(a)
    plot_function(a, b, step)


if __name__ == "__main__":
    main()
