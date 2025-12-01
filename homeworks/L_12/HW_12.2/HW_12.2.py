class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        # Повертаємо рядок з назвою та ціною товару.
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        # Повертаємо повне ім'я користувача.
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        # Формує багаторядковий звіт про замовлення.
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self):
        # Обчислює загальну вартість, перемножуючи ціну кожного товару на його кількість.
        return sum(item.price * cnt for item, cnt in self.products.items())

# Тестовий блок...
lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
buyer = User("Ivan", "Ivanov", "02628162")
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
assert cart.get_total() == 60
cart.add_item(apple, 10)
# Виправлений assert згідно з логікою (4*5 + 10*2 = 40)
assert cart.get_total() == 40