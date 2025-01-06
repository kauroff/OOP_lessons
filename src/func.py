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


class Product():
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
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    @classmethod
    def add_product(cls, product_data: dict):
        """
        Метод, который принимает товар и создает объект, который далее можно добавить в список товаров
        :param product_data: данные о товаре, представление в виде словаря
        :return: объект товара
        """
        return cls.__init__(**product_data)

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
        return self.price * self.quantity + other.price * other.quantity


class Generator():
    """
    Класс-генератор, необходимый для итерации по товарам в категории
    """
    def __init__(self, category):
        """
        :param category: категория, по которй будем итерироваться
        """
        self.category = category

    def __iter__(self):
        """
        Дандер-метод, создание генератора
        :return:
        """
        self.current_position = -1
        return self

    def __next__(self):
        """
        Дандер-метод, переход к следующей шагу
        :return:
        """
        if self.current_position + 1 < len(self.category):
            self.current_position += 1
            return category[self.current_position]
        else:
            raise StopIteration
