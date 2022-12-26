""" Модель "Покупатель" """
from decimal import Decimal


class Customer:

    def __init__(self, name: str, age: int, money: Decimal):
        self.name = name
        self.age = age
        self.money = money

    @property
    def is_adult(self):
        return self.age >= 18
