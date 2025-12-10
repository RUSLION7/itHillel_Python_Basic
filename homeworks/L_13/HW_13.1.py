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


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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

# Unit Test.
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')