""" Скрипты для интерактивного общения с пользователем """
from Shop import *


def _main():
    customer_data = input('Введите ваши данные в формате "Имя Деньги Возраст":\n')
    customer = Customer(*customer_data.split(' '))
    cart = Cart(customer)

    return input('Желаете продолжить?').strip()


if __name__ == '__main__':
    _main()
