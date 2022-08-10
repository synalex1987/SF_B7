class BoardException(Exception):
    def __repr__(self):
        return "Упс, ошибка. Проверьте ваш ввод, возможно вы ввели неправильные координаты"


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"
