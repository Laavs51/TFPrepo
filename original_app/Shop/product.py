""" Модель "Товар" """
from typing import Any, Dict


class Product:

    def __init__(self, name: str, price: float, for_adult: bool):
        self.name = name
        self.price = int(price)
        self.for_adult = for_adult

    @classmethod
    def from_json(cls, record: Dict[str, Any]):
        return cls(record['name'], record['price'], record['for_adult'])

    def __str__(self):
        return f'{self.name}: {self.price} у.е.'

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Any):
        if not isinstance(other, Product):
            return False

        return self.name == other.name and \
            self.price == other.price and \
            self.for_adult == other.for_adult
