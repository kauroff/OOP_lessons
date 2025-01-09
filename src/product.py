from abc_product import AbcProduct
from mixin import MixinRepr


class Product(AbcProduct, MixinRepr):
    """
    Класс для работы с товарами
    Включает в себя: имя, описание, цену, количество товара
    """
    name: str
    desc: str
    price: float
    quantity: int

    def __init__(self, name, desc, price, quantity):
        """
        :param name: имя
        :param desc: описание
        :param price: цена
        :param quantity: количество товара
        """
        super().__init__(name, desc, price, quantity)

    @classmethod
    def create_product(cls, product_data: dict):
        """
        Метод, который принимает товар и создает объект, который далее можно добавить в список товаров
        :param product_data: данные о товаре, представление в виде словаря
        :return: объект товара
        """
        return cls.__init__(**product_data)

    @classmethod
    def check_products(cls, product_data: dict):
        """
        Класс-метод, который проверяет наличие такого же товара.
        В случае совпадения складывает количество юнитов в наличии.
        При конфликте цен выбирает более высокую.
        :param product_data: данные о товаре в виде словаря
        :return:
        """
        if product_data['name'] not in [product['name'] for product in Category.check_products]:
            pass  # добавление товара
        else:
            pass

    @property
    def price(self):
        """
        Метод-геттер для цены товара
        :return: цену товара
        """
        return self.price

    @price.setter
    def set_price(self, value):
        """
        Метод-сеттер цены товара с проверкой на корректность введенных данных
        :param value: новое значение цены товара
        :return: сообщение об ошибке или изменение цены товара
        """
        if value <= 0:
            return 'Введена некорректная цена'
        elif value < self.price:
            answer = input('Вы уверены, что хотите снизить стоимость? Введите y-да, n-нет')
            if answer == 'y':
                self.price = value

    def __str__(self):
        """
        Дандер-метод для строкового отображения класса
        :return: строковое отображение
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """
        Дандер-метод для подсчета полной стоимости товаров
        :param other: стоиомсть других товаров
        :return: полную стоимость
        """
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
