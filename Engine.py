from math import tan


class Geometry:
    def __init__(self, x, y):
        self.center = (x, y)


class Point(Geometry):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __eq__(self, other):
        return self.center == other.center

    def __add__(self, other):
        return Point(self.center[0] + other.center[0],
                     self.center[1] + other.center[1])

    def __sub__(self, other):
        return Point(self.center[0] - other.center[0],
                     self.center[1] - other.center[1])

    def coord(self, x0=0, y0=0):
        return self - Point(x0, y0)


class Line(Geometry):
    def __init__(self, x_1, y_1, x_2, y_2):
        self.points = [Point(x_1, y_1), Point(x_2, y_2)]
        super().__init__(x_1 + (x_1 + x_2) // 2,
                         y_1 + (y_1 + y_2) // 2)

    def __eq__(self, other):
        if other.__class__ is Point:
            # Здесь нужно вывести формулу линейной функции по двум
            # точкам, а затем подставить и проверить является ли
            # точка частью этой прямой
            pass


class Area(Geometry):
    def __init__(self):
        super().__init__(0, 0)


class Object:
    def __init__(self):
        pass


class Thing(Object):
    def __init__(self):
        super().__init__()


class Prop(Thing):
    def __init__(self):
        super().__init__()


class HumansPart(Thing):
    def __init__(self):
        super().__init__()


class Location(Object):
    def __init__(self):
        super().__init__()


class DestroyableLocation(Location):
    def __init__(self):
        super().__init__()


a = Point(0, 2)
b = Line(12, 22, 323, 1)
print(b == a)
