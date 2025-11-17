def is_palindrome(text):
    """Перевіряє, чи є рядок паліндромом (ігноруючи регістр та пунктуацію)."""
    # Готуємо рядок для очищених символів.
    clean_string = ""

    # Перебираємо символи вхідного рядка.
    for char in text:
        # Залишаємо тільки літери та цифри, приводячи до нижнього регістру.
        if char.isalnum():
            clean_string += char.lower()

    # Порівнюємо очищений рядок з його перевернутою версією.
    return clean_string == clean_string[::-1]


# Unit Test.
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")