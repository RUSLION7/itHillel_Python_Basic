# Створюємо власний клас винятку.
class GroupLimitError(Exception):
    """Виняток для перевищення ліміту студентів у групі."""
    pass


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
        # Пошук і видалення студента за прізвищем.
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        # Пошук студента за прізвищем, повернення об'єкта або None.
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        # Формування рядка з інформацією про всіх студентів у групі.
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'