def second_index(text, some_str):
    # Шукаємо перше входження.
    first_index = text.find(some_str)

    # Якщо першого немає, то другого точно немає.
    if first_index == -1:
        return None

    # Шукаємо знову, але починаючи з позиції після першого входження.
    second_index = text.find(some_str, first_index + 1)

    # Повертаємо результат другого пошуку (індекс або -1).
    # Якщо .find() повернув -1, ми повертаємо None, інакше - сам індекс.
    if second_index == -1:
        return None
    else:
        return second_index


# Перевірочні тести.
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')