""" Модель " Магазин" """
import json
import os.path
from typing import Optional

from .product import Product


def _load_data():
    path = os.path.join(__file__, '../../storage.json')
    with open(os.path.normpath(path), encoding='utf-8') as file:
        return json.loads(file.read())


class Shop:

    def __init__(self):
        self.storage = {}
        self.products_by_name = {}

        for record in _load_data():
            product_name = record['name']
            self.storage[product_name] = record['num']
            self.products_by_name[product_name] = Product.from_json(record)

    def __str__(self):
        return '\n'.join(f'{product} у.е. - {num}' for product, num in self.storage.items())

    def check_product(self, product_name):
        return product_name in self.products_by_name

    def get_product(self, product_name: str) -> Optional[Product]:
        product = self.products_by_name.get(product_name)

        if product is None:
            return None

        if not self.storage[product_name]:
            return None

        return product

    def mark_collected(self, product_name):
        self.storage[product_name] -= 1
