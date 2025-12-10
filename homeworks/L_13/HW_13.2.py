class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        # Встановлюємо нове максимальне значення.
        self.max_value = max_max

    def set_min(self, min_min):
        # Встановлюємо нове мінімальне значення.
        self.min_value = min_min

    def step_up(self):
        # Викидаємо помилку, якщо досягнуто максимуму.
        if self.current == self.max_value:
            raise ValueError('Досягнуто максимум')
        # Інакше збільшуємо лічильник.
        self.current += 1

    def step_down(self):
        # Викидаємо помилку, якщо досягнуто мінімуму.
        if self.current == self.min_value:
            raise ValueError('Досягнуто мінімум')
        # Інакше зменшуємо лічильник.
        self.current -= 1

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'