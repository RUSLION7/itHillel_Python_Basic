import string

# Вхідний рядок для тестування.
user_input = "s-H"

# Еталонний алфавіт ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ').
all_letters = string.ascii_letters

# Отримуємо початковий та кінцевий символи з вхідного рядка.
start_char, end_char = user_input.split('-')

# Знаходимо їх індекси в еталонному алфавіті.
start_index = all_letters.index(start_char)
end_index = all_letters.index(end_char)

# Робимо зріз по знайдених індексах. +1 робить діапазон включним.
result = all_letters[start_index : end_index + 1]

print(f"Вхідний рядок: '{user_input}'")
print(f"Результат: {result}")