from src.product import Product


class Category:
    """
    Класс для работы с категориями товаров
    Включает в себя: имя, описание категории, список товаров; ведется подсчет категорий и уникальных продуктов
    Список продуктов - приватный атрибут
    """
    name: str
    desc: str
    __products: list
    count_category = 0
    uniq_products = 0

    def __init__(self, name, desc, products):
        """
        При инициализации увеличивается счетчик категорий и уникальных продуктов
        :param name: название категории
        :param desc: описание категории
        :param products: список продуктов
        """
        self.name = name
        self.desc = desc
        self.__products = products
        Category.count_category += 1
        Category.uniq_products += len(self.__products)

    @classmethod
    def add_product_in_category(cls, product: dict):  # не протестировано
        """
        Метод класса, необходимый для добавления продукта.
        Принимает объект товара и добавляет его в список
        __products: list
        :param product: объект товара
        :return: None / ошибка
        """
        product_cls = type(product)
        if issubclass(product_cls, Product) and isinstance(product, product_cls):
            # перепроверить
            if product.quantity == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            else:
                cls.__products.append(product)
                cls.uniq_products += 1

    @property
    def check_products(self):
        """
        Метод-геттер, который возвращает при вызове метода .products список товаров
        :return: список товаров
        """
        return self.__products

    @check_products.setter
    def set_products(self):  # не протестировано
        """
        Метод-сеттер, который устанавливает необходимые поля для товара
        :return:
        """
        pass

    @property
    def products(self):
        """
        Метод-геттер, который возвращает при вызове метода .products список товаров в заданном виде
        :return: список товаров в заданном формате в консоль
        """
        for product in self.__products:
            name = product['name']
            price = product['price']
            quantity = product['quantity']
            print(f'{name}, {price} руб. Остаток: {quantity} шт.')

    def __len__(self):
        """
        Дандер-метод для подсчета количества продуктов в категории
        :return: количество продуктов
        """
        count = 0
        for product in self.__products:
            count += product['quantity']
        return count

    def __str__(self):
        """
        Дандер-метод для строкового отображения класса
        :return: строковое отображение
        """
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def average_price(self):
        """
        Метод, который подсчитывает средний ценник всех товаров в категории.
        :return: средний ценник / 0
        """
        count_prod = 0
        total_price = 0
        for product in self.__products:
            count_prod += product['quantity']
            total_price
        try:
            return total_price / count_prod
        except:
            return 0
