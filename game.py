from Player import *
from board import *

default_numbers_of_ships = [3, 2, 2, 1, 1, 1, 1]
max_attempts = 3000


class Game:
    def __init__(self, size=default_board_size):
        self.size = size
        player_board: Board = self.random_board()
        enemy_board: Board = self.random_board()
        player_board.display = True
        self.player = User(player_board, enemy_board)
        self.enemy = Computer(enemy_board, player_board)

    def random_board(self):
        b = None
        while b is None:
            b = self.random_places()
        return b

    def random_places(self):
        ships = default_numbers_of_ships
        board = Board(size=self.size)
        attempts = 0
        for len_ship in ships:
            while True:
                attempts += 1
                if attempts > max_attempts:
                    return None
                ship = Ship(Cell(randint(0, self.size - 1), randint(0, self.size - 1)), randint(0, 1), len_ship)
                try:
                    board.add_ship(ship)
                    break
                except BoardException:
                    pass
        board.ships_area = []
        return board

    @staticmethod
    def say_hi():
        print("<<<<Морской бой>>>>")
        print("Формат ввода, 2 цифры: x y")
        print("x - номер строки")
        print("y - номер столбца")

    def loop(self):
        num = 0
        while True:
            print("*" * 10)
            print("Доска игрока:")
            print(self.player.my_board)
            print("*" * 10)
            print("Доска компьютера:")
            print(self.enemy.my_board)
            if num % 2 == 0:
                print("*" * 10)
                print("Ходит игрок!")
                repeat = self.player.move()
            else:
                print("*" * 10)
                print("Ходит компьютер!")
                repeat = self.enemy.move()
            if repeat:
                num -= 1

            if self.enemy.my_board.dead_ships == 7:
                print("*" * 10)
                print("Игрок выиграл!")
                break

            if self.player.my_board.dead_ships == 7:
                print("*" * 10)
                print("Компьютер выиграл!")
                break
            num += 1
            #print(f'enemy dead_ships: {self.enemy.my_board.dead_ships}; my dead ships: {self.player.my_board.dead_ships}')

    def start(self):
        self.say_hi()
        self.loop()
