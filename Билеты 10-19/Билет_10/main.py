class ZDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


class Session:
    def __init__(self, date, teacher, group, subject):
        self.date = date
        self.teacher = teacher
        self.group = group
        self.subject = subject

    def __str__(self):
        return f"{self.subject} ({self.group}) - {self.date} - Преподаватель: {self.teacher}"


def print_schedule(sessions):
    print("График сдачи экзаменов:")
    for session in sessions:
        print(session)


if __name__ == "__main__":
    date1 = ZDate(15, 5, 2024)
    date2 = ZDate(20, 5, 2024)
    date3 = ZDate(25, 5, 2024)

    session1 = Session(date1, "Иванов", "Группа 1", "Математика")
    session2 = Session(date2, "Петров", "Группа 2", "Физика")
    session3 = Session(date3, "Сидорова", "Группа 1", "Химия")

    print_schedule([session1, session2, session3])
