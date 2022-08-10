from cell import Cell
from ship import Ship
from BoardException import BoardException, BoardOutException, BoardUsedException

default_board_size = 6


# ■ - обозначение корабля. 0 - пустая клетка(или доска скрыта)
class Board:
    def __init__(self, display=False, size=default_board_size):
        self.size = size
        self.display = display
        self.field = [["0"]*size for _ in range(size)]
        self.ships = []
        self.ships_area = []
        self.dead_ships = 0

    def __repr__(self):
        res = "  | "
        for i in range(self.size):
            res += f"{i + 1} | "
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if not self.display:
            res = res.replace("■", "0")
        return res

    # проверить, что переданная ячейка попадает в область доски
    def check_out(self, cell: Cell) -> bool:
        return not ((0 <= cell.x < self.size) and (0 <= cell.y < self.size))

    # заполнить ships_area; обозначить область в 1 точку от корабля недоступной для стрельбы
    def ship_area(self, s: Ship, display=False):
        area = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]
        for cell in s.location:
            for x, y in area:
                check_cell = Cell(cell.x + x, cell.y + y)
                if not (self.check_out(check_cell)) and check_cell not in self.ships_area:
                    if display:
                        self.field[check_cell.x][check_cell.y] = "."
                    self.ships_area.append(check_cell)

    # Поставить корабль на поле
    def add_ship(self, s: Ship):
        for cell in s.location:
            if self.check_out(cell) or cell in self.ships_area:
                raise BoardException()
        for cell in s.location:
            self.field[cell.x][cell.y] = "■"
            self.ships_area.append(cell)

        self.ships.append(s)
        self.ship_area(s)

    def check_shot(self, cell: Cell) -> bool:
        if self.check_out(cell):
            raise BoardOutException()
        if cell in self.ships_area:
            raise BoardUsedException()

        self.ships_area.append(cell)

        for s in self.ships:
            if cell in s.location:
                s.lives -= 1
                self.field[cell.x][cell.y] = "X"
                if s.lives == 0:
                    self.dead_ships += 1
                    self.ship_area(s, display=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[cell.x][cell.y] = "."
        print("Мимо!")
        return False
