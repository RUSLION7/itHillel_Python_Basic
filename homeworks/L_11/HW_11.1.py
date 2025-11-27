def prime_generator(end):
    """Генерує прості числа до заданої межі `end`."""
    # Перебираємо кандидатів на просте число.
    for n in range(2, end + 1):
        # Припускаємо, що число просте.
        is_prime = True
        # Перевіряємо наявність дільників.
        for d in range(2, n):
            if n % d == 0:
                # Якщо дільник знайдено, число не просте.
                is_prime = False
                break

        # Якщо дільників не знайдено, "видаємо" просте число.
        if is_prime:
            yield n


# Unit Test.
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('OK')