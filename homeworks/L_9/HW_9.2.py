def difference(*args):
    """Повертає різницю між max і min елементом з переданих аргументів."""
    # Перевіряємо, чи були передані аргументи.
    if not args:
        # Якщо ні, повертаємо 0.
        return 0

    # Обчислюємо різницю між максимальним і мінімальним значеннями.
    result = max(args) - min(args)

    # Округлюємо результат і повертаємо його.
    return round(result, 2)


# Unit Test для перевірки.
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('ОК')