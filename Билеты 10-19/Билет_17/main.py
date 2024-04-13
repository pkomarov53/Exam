class Vector:
    def __init__(self, elements):
        self.elements = elements

    def merge(self, other):
        merged_vector = []
        i = 0
        j = 0

        while i < len(self.elements) and j < len(other.elements):
            if self.elements[i] < other.elements[j]:
                merged_vector.append(self.elements[i])
                i += 1
            else:
                merged_vector.append(other.elements[j])
                j += 1

        while i < len(self.elements):
            merged_vector.append(self.elements[i])
            i += 1

        while j < len(other.elements):
            merged_vector.append(other.elements[j])
            j += 1

        return Vector(merged_vector)

    def __str__(self):
        return str(self.elements)


# Пример использования
vector1 = Vector([1, 3, 5, 7, 9])
vector2 = Vector([2, 4, 6, 8, 10])

merged_vector = vector1.merge(vector2)
print(f'Vector 1: {vector1}\nVector 2: {vector2}')
print("Merged Vector:", merged_vector)
