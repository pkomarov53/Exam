class ZTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return ZTime.from_seconds(total_seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return cls(hours, minutes, seconds)

if __name__ == "__main__":
    class Student:
        def __init__(self, name, time):
            self.name = name
            self.time = time

        def __str__(self):
            return f"{self.name}: {self.time}"


    students = [
        Student("Андрей", ZTime(0, 3, 15)),
        Student("Мария", ZTime(0, 3, 30)),
        Student("Иван", ZTime(0, 3, 45)),
    ]

    print("Результаты 1000-метрового забега:")
    for student in students:
        print(student)
