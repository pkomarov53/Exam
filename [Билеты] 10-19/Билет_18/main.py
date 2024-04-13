class StudentList:
    def __init__(self, elements):
        self.elements = elements

    def take_exam(self, student_id, grade):
        for i, record in enumerate(self.elements):
            if record[0] == student_id:
                self.elements.pop(i)
                self.elements.insert(i, (student_id, record[1], grade))
                return True
        return False

    def __str__(self):
        return str(self.elements)


List1 = StudentList([(123, "Smith"), (124, "Johnson"), (125, "Williams")])
List2 = StudentList([])

List1.take_exam(123, 4)
List1.take_exam(124, 5)
List1.take_exam(125, 3)

print("List1:", List1)
print("List2:", List2)
