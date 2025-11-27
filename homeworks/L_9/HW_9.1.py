def popular_words(text, words):
    """Підраховує популярність заданих слів у тексті, ігноруючи регістр."""
    # Готуємо текст: приводимо до нижнього регістру та розбиваємо на слова.
    text_words = text.lower().split()

    # Створюємо словник-лічильник з початковими нулями.
    word_counts = {}
    for word in words:
        word_counts[word] = 0

    # Перебираємо слова з тексту та оновлюємо лічильники.
    for text_word in text_words:
        if text_word in word_counts:
            word_counts[text_word] += 1

    # Повертаємо заповнений словник.
    return word_counts


# Unit Test.
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')