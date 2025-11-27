# Вхідні дані для тестування.
total_seconds = 224930

# Визначаємо константи.
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

# Розраховуємо дні, години, хвилини, секунди.
days, remaining_seconds = divmod(total_seconds, SECONDS_IN_DAY)
hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)

# Визначаємо правильну форму слова "день".
if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"

# Форматуємо час, додаючи ведучі нулі.
formatted_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

# Формуємо і виводимо фінальний результат.
result = f"{days} {day_word}, {formatted_time}"

print(f"Початковий список: {total_seconds}")
print(f"Результат: {result}")