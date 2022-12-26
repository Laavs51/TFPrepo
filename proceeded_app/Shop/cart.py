""" Модель "Корзина" """
from typing import Dict

from .customer import Customer
from .product import Product
from .shop import Shop


def can_afford(money: int, items: Dict[Product, int], product: Product) -> bool:
    total_value = sum((item.price * num for item, num in items.items()), product.price)
    return money >= total_value


def get_shopping_list(items: Dict[Product, int]) -> str:
    return '\n'.join(f'{product} - {num}' for product, num in items.items())


def get_total_cost(items: Dict[Product, int]) -> int:
    return sum(product.price * num for product, num in items.items())


def get_money_remains(money: int, total_cost: int) -> int:
    return money - total_cost


def get_cart_msg(money: int, items: Dict[Product, int]):
    cart_result = get_shopping_list(items)
    total_cost = get_total_cost(items)
    money_remains = get_money_remains(money, total_cost)
    return f'\n{cart_result}' \
           f'\nИтого: {total_cost} у.е.' \
           f'\nОсталось: {money_remains} у.е.'


def add(items: Dict[Product, int], product: Product):
    if product not in items:
        items.update({product: 1})
        return items
    return {prod: num + 1 if prod == prod else num
            for prod, num in items.items()}


def remove(storage: Dict[str, int], product_name: str):
    return {name: num - 1 if name == product_name else num
            for name, num in storage.items()}


class Cart:

    def __init__(self, customer: Customer):
        self.shop = Shop()
        self.customer = customer
        self.items = dict()

    def __str__(self):
        return get_cart_msg(self.customer.money, self.items)

    def add(self, product_name: str):
        product = self.shop.get_product(product_name)

        if product is None:
            return False

        if not can_afford(self.customer.money, self.items, product):
            return False

        if self.is_forbidden_for_customer(product):
            return False

        self.items = add(self.items, product)
        self.shop.storage = remove(self.shop.storage, product_name)
        return True

    def can_afford(self, product: Product) -> bool:
        total_value = sum((item.price * num for item, num in self.items.items()), product.price)
        return self.customer.money >= total_value

    def is_forbidden_for_customer(self, product: Product) -> bool:
        return product.for_adult and not self.customer.is_adult
