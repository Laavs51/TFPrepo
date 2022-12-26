""" Скрипты для интерактивного общения с пользователем """
from Shop import Cart, Customer


def _main():
    customer_data = input('Введите ваши данные в формате "Имя Возраст Деньги":\n')
    cust = Customer(*customer_data.split(' '))
    shopping_cart = Cart(cust)
    print(f'Ассортимент:\n{shopping_cart.shop}')

    while True:
        product_name = input('Введите имя добавляемого товара: ')

        if not product_name:
            break

        added = shopping_cart.add(product_name)
        if not added:
            print('Товар не удалось добавить')

    print(f'\n{shopping_cart}\n')
    input('Для завершения работы нажмите любую кнопку')


if __name__ == '__main__':
    _main()
