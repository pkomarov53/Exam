import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic_function(coefficients, step):
    a, b, c = coefficients
    x = np.arange(-10, 10, step)
    y = a * x**2 + b * x + c

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Quadratic Function: {a}x^2 + {b}x + {c}')
    plt.grid(True)
    plt.show()

def main():
    # Чтение коэффициентов и шага из строки
    with open('coefficients.txt', 'r') as file:
        data = file.readline().split()
        coefficients = list(map(float, data[:-1]))  # Коэффициенты
        step = float(data[-1])  # Шаг сетки

    plot_quadratic_function(coefficients, step)

if __name__ == "__main__":
    main()
