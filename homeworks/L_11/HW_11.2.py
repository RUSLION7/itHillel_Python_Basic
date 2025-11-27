def generate_cube_numbers(end):
    """Генерує куби чисел від 2, доки результат менше `end`."""
    # Початкове число для зведення в куб.
    number = 2

    # Цикл для генерації послідовності.
    while True:
        # Обчислюємо куб.
        cube = number ** 3
        # Перевіряємо, чи не перевищено межу.
        if cube >= end:
            # Зупиняємо генератор.
            return
        # "Видаємо" результат.
        yield cube
        # Переходимо до наступного числа.
        number += 1


# Unit Test.
from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], '10 у кубі це 1000'
print('OK')