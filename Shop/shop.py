""" Модель " Магазин" """
import json
from typing import Optional

from .product import Product


def _load_data():
    with open('../storage.json', encoding='utf-8') as file:
        return json.loads(file.read())


class Shop:

    def __init__(self):
        self.data = {Product.from_json(record): record['num']
                     for record in _load_data()}

    def get_product(self, product_name: str) -> Optional[Product]:
        product = next((item for item in self.data if item.name == product_name), None)

        if product is None:
            return None

        self.data[product] -= 1

        if not self.data[product]:
            del self.data[product]

        return product
