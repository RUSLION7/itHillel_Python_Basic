import keyword
import string

user_input = input("Введіть рядок для перевірки: ")

# Створюємо "прапор" валідності (принцип "презумпції невинуватості")
is_valid = True

# Перевірка 0: Порожній рядок не є валідним ім'ям.
if not user_input:
    is_valid = False

# Якщо рядок вже невалідний, подальші перевірки не мають сенсу.
if is_valid:
    # Перевірка 1: Чи не є рядок зарезервованим словом.
    if user_input in keyword.kwlist:
        is_valid = False

# Продовжуємо перевірки, тільки якщо рядок все ще вважається валідним.
if is_valid:
    # Перевірка 2: Чи не починається рядок з цифри.
    if user_input[0].isdigit():
        is_valid = False

# Продовжуємо перевірки...
if is_valid:
    # Перевірка 3: Спеціальне правило для рядків, що складаються тільки з '_'.
    # Якщо кількість '_' дорівнює довжині рядка, і довжина більша за 1.
    if user_input.count('_') == len(user_input) and len(user_input) > 1:
        is_valid = False

# Продовжуємо перевірки...
if is_valid:
    # Перевірка 4: Перевірка кожного символу на допустимість.
    for char in user_input:
        # Символ невалідний, якщо він є:
        # а) великою літерою
        is_uppercase = char.isupper()
        # б) пробілом
        is_space = char == ' '
        # в) знаком пунктуації, але не нижнім підкресленням
        is_punctuation = char in string.punctuation and char != '_'

        # Якщо хоча б одна з цих умов істинна, то символ невалідний.
        if is_uppercase or is_space or is_punctuation:
            is_valid = False
            # Якщо знайдено хоча б один невалідний символ, подальша перевірка не потрібна.
            break

print(is_valid)