def add_one(some_list):
    """Перетворює список цифр на число, додає 1, і повертає результат у вигляді списку."""
    # Перетворюємо список на рядок, а потім на число.
    number = int("".join([str(d) for d in some_list]))

    # Додаємо 1 і перетворюємо результат назад на рядок.
    result_string = str(number + 1)

    # Перетворюємо рядок результату назад на список цілих чисел.
    return [int(d) for d in result_string]


# Unit Test для перевірки.
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")