class Polynom:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if degree - i > 1:
                    terms.append(f"{coeff}x^{degree - i}")
                elif degree - i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(str(coeff))
        return " + ".join(terms)

    def __add__(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_length - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_length - len(other.coefficients))
        sum_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynom(sum_coefficients)

    def derivative(self):
        derivative_coeffs = [i * coeff for i, coeff in enumerate(self.coefficients)][1:]
        return Polynom(derivative_coeffs)


if __name__ == "__main__":
    poly1 = Polynom([1, 2, 3])
    poly2 = Polynom([0, -1, 2])

    sum_poly = poly1 + poly2
    print("Сумма полиномов:", sum_poly)

    derivative_poly = poly1.derivative()
    print("Производная полинома:", derivative_poly)
