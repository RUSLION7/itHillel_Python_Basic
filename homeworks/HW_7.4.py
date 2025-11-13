def common_elements():
    # Створюємо множину чисел, кратних 3 (0-99).
    set_of_threes = {i for i in range(100) if i % 3 == 0}

    # Створюємо множину чисел, кратних 5 (0-99).
    set_of_fives = {i for i in range(100) if i % 5 == 0}

    # Повертаємо перетин (спільні елементи) цих двох множин.
    return set_of_threes & set_of_fives



assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("ОК")