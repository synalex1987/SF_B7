from cell import Cell


class Ship:
    # first_point - первая точка корабля
    # direction - направление корабля. 0 - вертикальное, 1 - горизонтальное
    # lives - жизнь(длина) корабля
    def __init__(self, first_point, direction=0, lives=1):
        self.first_point = first_point
        self.direction = direction
        self.lives = lives
        self.location = []
        for i in range(self.lives):
            _x = self.first_point.x
            _y = self.first_point.y
            if self.direction == 0:
                _x += i
            elif self.direction == 1:
                _y += i
            self.location.append(Cell(_x, _y))

    @property
    def get_location(self) -> list:
        return self.location

    def check_shot(self, shot: Cell) -> bool:
        return shot in self.location
