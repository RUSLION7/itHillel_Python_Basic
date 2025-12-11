# Створюємо власний клас винятку.
class GroupLimitError(Exception):
    """Виняток для перевищення ліміту студентів у групі."""
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {super().__str__()}, Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Перевіряємо ліміт перед додаванням.
        if len(self.group) >= 10:
            # Якщо ліміт перевищено, генеруємо помилку.
            raise GroupLimitError("Неможливо додати більше 10 студентів до групи.")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'

# Тестування винятку.
gr = Group('TestGroup')
for i in range(10):
    gr.add_student(Student('Any', 20, f'Name{i}', f'Surname{i}', f'Book{i}'))

try:
    eleventh_student = Student('Any', 21, 'Extra', 'Student', 'ExtraBook')
    gr.add_student(eleventh_student)
except GroupLimitError as e:
    print(f"Виняток успішно перехоплено: {e}")

assert len(gr.group) == 10
print("Тест пройдено.")