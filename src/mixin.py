class MixinRepr:
    """
    Микси-класс, который выводит информацию в консоль о том, что был создан объект
    """

    def __repr__(self):
        """
        Дандер-метод для вывода отладочной информации
        :return: отладочная инфа
        """
        data = [unit for unit in vars(self).values()]
        return f'{type(self).__name__}({data})'
