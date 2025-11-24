def first_word(text):
    """ Пошук першого слова """
    # Замінюємо всі крапки та коми на пробіли.
    cleaned_text = text.replace('.', ' ').replace(',', ' ')

    # Розбиваємо очищений рядок на список слів.
    words = cleaned_text.split()

    # Повертаємо перше слово зі списку.
    return words[0]


# Unit Test.
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')