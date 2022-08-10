from random import randint
from board import Board
from board import default_board_size
from BoardException import BoardException
from cell import Cell


class Player:
    def __init__(self, board: Board, enemy: Board):
        self.my_board = board
        self.enemy_board = enemy

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.check_shot(target)
                return repeat
            except BoardException:
                print('Проверьте введенные координаты')


class Computer(Player):
    def ask(self):
        с = Cell(randint(0, self.enemy_board.size - 1), randint(0, self.enemy_board.size - 1))
        print(f"Ход компьютера: {с.x + 1} {с.y + 1}")
        return с


class User(Player):
    def ask(self):
        while True:
            cords = input("Введите координаты: ").split()
            if len(cords) != 2:
                print("Введите 2 координаты! (x, y)")
                continue
            x, y = cords
            if not (x.isdigit()) or not (y.isdigit()):
                print("Попробуйте ввести данные ещё раз. Неверный формат!")
                continue

            x, y = int(x), int(y)
            return Cell(x - 1, y - 1)

