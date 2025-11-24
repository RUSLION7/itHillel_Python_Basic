def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    # Поточне значення починається з `begin`.
    current_value = begin

    # Повторюємо цикл `end` разів.
    for _ in range(end):
        # Повертаємо поточне значення.
        yield current_value
        # Оновлюємо значення для наступної ітерації.
        current_value = func(current_value)


# --- Unit Test ---
def pow(x):
    return x ** 2


from inspect import isgenerator

gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('ОК')