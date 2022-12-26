""" Модель "Корзина" """
from collections import defaultdict

from .customer import Customer
from .product import Product
from .shop import Shop


class Cart:

    def __init__(self, customer: Customer):
        self.owner = Shop()
        self.customer = customer
        self.items = defaultdict(int)

    def __str__(self):
        cart_result = '\n'.join(f'{product} - {num}' for product, num in self.items.items())
        total_cost = sum(product.price * num for product, num in self.items.items())
        money_remains = self.customer.money - total_cost
        return f'{cart_result}' \
               f'Итого: {total_cost}' \
               f'Осталось: {money_remains}'

    def add(self, product_name: str):
        product = self.owner.get_product(product_name)

        if product is None:
            return False

        if not self.can_afford(product):
            return False

        if self.is_forbidden_for_customer(product):
            return False

        self.items[product] += 1
        return True

    def can_afford(self, product: Product) -> bool:
        cart_value = sum(self.items.values())
        return self.customer.money >= cart_value + product.price

    def is_forbidden_for_customer(self, product: Product) -> bool:
        return not product.for_adult or self.customer.is_adult
