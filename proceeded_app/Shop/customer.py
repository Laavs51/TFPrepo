""" Модель "Покупатель" """


class Customer:

    def __init__(self, name: str, age: int, money: str):
        self.name = name
        self.age = int(age)
        self.money = int(money)

    @property
    def is_adult(self):
        return self.age >= 18
