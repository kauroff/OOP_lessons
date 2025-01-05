class Category():
    name: str
    desc: str
    products: list
    count_category = 0
    uniq_products = 0

    def __init__(self, name, desc, products):
        self.name = name
        self.desc = desc
        self.products = products


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
