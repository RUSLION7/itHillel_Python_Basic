import codecs
import os


def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Визначаємо папку, де знаходиться скрипт.
    script_dir = os.path.dirname(__file__)
    # Формуємо повні шляхи до вхідного та вихідного файлів.
    html_file_path = os.path.join(script_dir, html_file)
    result_file_path = os.path.join(script_dir, result_file)

    # Читаємо вхідний файл.
    with codecs.open(html_file_path, 'r', 'utf-8') as file:
        html = file.read()

    # Фільтруємо символи, залишаючи тільки ті, що поза тегами.
    text_without_tags = ""
    in_tag = False
    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            text_without_tags += char

    # Видаляємо порожні рядки та збираємо очищений текст.
    cleaned_text = "\n".join([line for line in text_without_tags.splitlines() if line.strip()])

    # Записуємо очищений текст у вихідний файл.
    with codecs.open(result_file_path, 'w', 'utf-8') as file:
        file.write(cleaned_text)


# Виклик функції.
delete_html_tags('draft.html')