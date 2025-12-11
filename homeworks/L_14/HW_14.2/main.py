# Імпортуємо необхідні класи.
from human_student import Student
from group import Group

# Створюємо екземпляри студентів.
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створюємо групу.
gr = Group('PD1')

# Додаємо студентів до групи.
gr.add_student(st1)
gr.add_student(st2)

# Виводимо початковий склад групи.
print(gr)

# Тест: пошук існуючого студента (перевірка роботи __eq__).
assert gr.find_student('Jobs') == st1
# Тест: пошук неіснуючого студента.
assert gr.find_student('Jobs2') is None

# Видаляємо студента.
gr.delete_student('Taylor')

# Виводимо оновлений склад групи.
print("\nAfter deleting Taylor:")
print(gr) # Only one student