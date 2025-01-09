from product import Product


class Smartphone(Product):
    """
    Наслденик класса Product с дополнительными полями
    """
    power: int
    model: str
    mem: int
    color: str

    def __init__(self, name, desc, price, quantity, power, model, mem, color):
        super().__init__(name, desc, price, quantity)
        self.power = power
        self.model = model
        self.mem = mem
        self.color = color
