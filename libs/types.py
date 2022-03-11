from math import cos, sin


class Color:

    def __init__(self, r: int, g: int, b: int):
        self.color = (r, g, b)

    def set(self, r: int, g: int, b: int):
        self.color = (r, g, b)


class Coordinates:

    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def set(self, x: float, y: float):
        self.x, self.y = x, y


class Vector:

    def __init__(self, c1: Coordinates = None, c2: Coordinates = None, length: float = None, ang: float = None):
        # only coordinates
        if (c1 is not None) and (c2 is not None):
            self.x, self.y = c2.x - c1.x, c2.y - c1.y
        # length and angle
        elif (length is not None) and (ang is not None):
            self.x, self.y = length * cos(ang), length * sin(ang)
        # only angle
        elif ang is not None:
            self.x, self.y = cos(ang), sin(ang)
        # you give wrong params
        else:
            raise Exception

    def section(self, start_x: float, start_y: float):
        return Coordinates(start_x, start_y), Coordinates(start_x + self.x, start_y + self.y)


