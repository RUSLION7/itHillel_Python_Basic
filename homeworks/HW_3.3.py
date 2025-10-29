# --- Приклад 1: Парна кількість елементів ---
list_1 = [1, 2, 3, 4, 5, 6]
print(f"Початковий список: {list_1}")

# Визначаємо точку розділення
split_index_1 = (len(list_1) + 1) // 2  # (6 + 1) // 2 = 3

# Використовуємо зрізи для створення двох половин
first_half_1 = list_1[:split_index_1]  # Елементи з 0 до 3 (не включно) -> [1, 2, 3]
second_half_1 = list_1[split_index_1:] # Елементи з 3 до кінця -> [4, 5, 6]

# Створюємо підсумковий список
result_1 = [first_half_1, second_half_1]
print(f"Кінцевий список:   {result_1}")
print("-" * 30)


# --- Приклад 2: Непарна кількість елементів (короткий) ---
list_2 = [1, 2, 3]
print(f"Початковий список: {list_2}")

split_index_2 = (len(list_2) + 1) // 2  # (3 + 1) // 2 = 2
first_half_2 = list_2[:split_index_2]  # -> [1, 2]
second_half_2 = list_2[split_index_2:] # -> [3]

result_2 = [first_half_2, second_half_2]
print(f"Кінцевий список:   {result_2}")
print("-" * 30)


# --- Приклад 3: Непарна кількість елементів (довгий) ---
list_3 = [1, 2, 3, 4, 5]
print(f"Початковий список: {list_3}")

split_index_3 = (len(list_3) + 1) // 2  # (5 + 1) // 2 = 3
first_half_3 = list_3[:split_index_3]  # -> [1, 2, 3]
second_half_3 = list_3[split_index_3:] # -> [4, 5]

result_3 = [first_half_3, second_half_3]
print(f"Кінцевий список:   {result_3}")
print("-" * 30)


# --- Приклад 4: Один елемент ---
list_4 = [1]
print(f"Початковий список: {list_4}")

split_index_4 = (len(list_4) + 1) // 2  # (1 + 1) // 2 = 1
first_half_4 = list_4[:split_index_4]  # -> [1]
second_half_4 = list_4[split_index_4:] # -> []

result_4 = [first_half_4, second_half_4]
print(f"Кінцевий список:   {result_4}")
print("-" * 30)


# --- Приклад 5: Порожній список (особливий випадок) ---
list_5 = []
print(f"Початковий список: {list_5}")

# (0 + 1) // 2 = 0
split_index_5 = (len(list_5) + 1) // 2
first_half_5 = list_5[:split_index_5]  # -> []
second_half_5 = list_5[split_index_5:] # -> []

result_5 = [first_half_5, second_half_5]
print(f"Кінцевий список:   {result_5}")
print("-" * 30)