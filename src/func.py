class Category():
    name: str
    desc: str
    __products: list
    count_category = 0
    uniq_products = 0

    def __init__(self, name, desc, products):
        self.name = name
        self.desc = desc
        self.__products = products
        Category.count_category += 1
        Category.uniq_products += len(self.__products)

    @classmethod
    def add_product(cls, product):
        cls.__products.append(product)
        cls.uniq_products += 1

    @property
    def products(self):
        for product in self.__products:
            name = product['name']
            price = product['price']
            quantity = product['quantity']
            print(f'{name}, {price} руб. Остаток: {quantity} шт.')

    def __len__(self):
        return len(self.__products[2])

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'


class Product():
    name: str
    desc: str
    price: float
    quantity: int

    def __init__(self, name, desc, price, quantity):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    @classmethod
    def add_product(cls, product_data: dict):
        return cls.__init__(**product_data)

    @property
    def price(self):
        return self.price

    @price.setter
    def set_price(self, value):
        if value <= 0:
            return 'Введена некорректная цена'
        elif value < self.price:
            answer = input('Вы уверены, что хотите снизить стоимость? Введите y-да, n-нет')
            if answer == 'y':
                self.price = value

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


class Generator():
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_position = -1
        return self

    def __neg__(self):
        if self.current_position + 1 < len(self.category):
            self.current_position += 1
            return category[self.current_position]
        else:
            raise StopIteration
