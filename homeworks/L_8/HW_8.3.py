def find_unique_value(some_list):
    """Знаходить та повертає єдиний унікальний елемент у списку."""
    # Перебираємо кожен елемент у списку.
    for number in some_list:
        # Рахуємо, скільки разів елемент зустрічається у списку.
        # Якщо лічильник дорівнює 1, це унікальний елемент.
        if some_list.count(number) == 1:
            # Повертаємо знайдений елемент.
            return number

# Unit Test для перевірки.
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")