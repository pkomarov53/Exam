import matplotlib.pyplot as plt
import numpy as np


def plot_function(a, b, step):
    x = np.arange(0.01, 1, step)  # Избегаем значения x равного 0
    y = a * (np.log(x) ** 2) + b

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График функции y = {} * ln^2(x) + {}'.format(a, b))
    plt.grid(True)
    plt.show()


def main():
    with open('coefficients.txt', 'r') as file:
        coefficients = file.readline().strip().split()
    a = float(coefficients[0])
    b = float(coefficients[1])
    step = float(coefficients[2])

    plot_function(a, b, step)


if __name__ == "__main__":
    main()
