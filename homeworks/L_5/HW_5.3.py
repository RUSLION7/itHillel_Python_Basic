# --- Початкові дані для тестування ---
# Щоб перевірити інший випадок з прикладу, змініть значення цього рядка.
user_input = 'i like python community!'

print(f"Початковий рядок: '{user_input}'")

# Метод .title() робить першу літеру кожного слова великою, а решту - малими.
title_cased_string = user_input.title()
# title_cased_string тепер: 'I Like Python Community!'

# --- Видалення всіх символів, окрім літер та цифр ---
# Створюємо порожній список для зберігання "чистих" символів.
clean_chars = []
# Перебираємо кожен символ у рядку.
for char in title_cased_string:
    # Метод .isalnum() перевіряє, чи є символ літерою або цифрою.
    if char.isalnum():
        # Якщо так, додаємо його до нашого списку.
        clean_chars.append(char)
# clean_chars тепер: ['I', 'L', 'i', 'k', 'e', 'P', 'y', 't', 'h', 'o', 'n', 'C', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y']

# --- Створення основи хештегу ---
# Метод .join() об'єднує всі елементи списку в один суцільний рядок.
hashtag_body = "".join(clean_chars)
# hashtag_body тепер: 'ILikePythonCommunity'

# --- Додавання символу # ---
# Додаємо символ '#' на початок.
raw_hashtag = '#' + hashtag_body
# raw_hashtag тепер: '#ILikePythonCommunity'

# --- Перевірка довжини та обрізка ---
# Перевіряємо, чи довжина хештегу не перевищує 140 символів.
if len(raw_hashtag) > 140:
    # Якщо довжина більша, використовуємо зріз, щоб залишити тільки перші 140 символів.
    final_hashtag = raw_hashtag[:140]
else:
    # В іншому випадку, хештег залишається без змін.
    final_hashtag = raw_hashtag

print(f"Результат: {final_hashtag}")