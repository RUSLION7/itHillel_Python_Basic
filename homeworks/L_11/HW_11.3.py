def is_even(number):
    """Перевіряє число на парність за допомогою побітових операцій."""
    # Перевіряємо, чи дорівнює останній біт числа нулю.
    # Якщо так, число парне.
    return (number & 1) == 0

# Unit Test.
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')