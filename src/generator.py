class Generator:
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
