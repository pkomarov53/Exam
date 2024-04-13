class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Ошибка: деление на ноль"
        return x / y

def main():
    calculator = Calculator()
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Введите номер операции: ")
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if choice == '1':
                print("Результат:", calculator.add(num1, num2))
            elif choice == '2':
                print("Результат:", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Результат:", calculator.multiply(num1, num2))
            elif choice == '4':
                print("Результат:", calculator.divide(num1, num2))
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию от 1 до 5.")

if __name__ == "__main__":
    main()
