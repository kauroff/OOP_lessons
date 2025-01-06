class Category():
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
    def add_product_in_category(cls, product):
        """
        Метод класса, необходимый для добавления продукта.
        Принимает объект товара и добавляет его в список
        __products: list
        :param product: объект товара
        :return: None
        """
        cls.__products.append(product)
        cls.uniq_products += 1

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
        return len(self.__products[2])

    def __str__(self):
        """
        Дандер-метод для строкового отображения класса
        :return: строковое отображение
        """
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'
