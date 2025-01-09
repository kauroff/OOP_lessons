from abc import ABC, abstractmethod


class AbcProduct(ABC):
    @abstractmethod
    def __init__(self, name, desc, price, quantity):
        """
        :param name: имя
        :param desc: описание
        :param desc: описание
        :param price: цена
        :param quantity: количество товара
        """
        self.name = name
        self.desc = desc
        self.__price = price
        self.quantity = quantity
