class Human:
    def __init__(self, gender, age, first_name, last_name):
        # Ініціалізація атрибутів людини.
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        # Рядкове представлення людини.
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        # Виклик конструктора батьківського класу.
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        # Перевизначене рядкове представлення для студента.
        return f"Student: {super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        # Метод для порівняння об'єктів (необхідний для assert).
        return str(self) == str(other)

    def __hash__(self):
        # Метод для хешування (необхідний для додавання в set).
        return hash(str(self))