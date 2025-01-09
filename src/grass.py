from product import Product


class LawnGrass(Product):
    """
    Наслденик класса Product с дополнительными полями
    """
    country: str
    time: int
    color: str

    def __init__(self, name, desc, price, quantity, country, time, color):
        super().__init__(name, desc, price, quantity)
        self.country = country
        self.time = time
        self.color = color
