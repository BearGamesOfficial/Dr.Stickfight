class Geometry:
    def __init__(self, x, y):
        self.center = (x, y)


class Point(Geometry):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __eq__(self, other):
        return self.center == other.center


class Line(Geometry):
    def __init__(self, x_1, y_1, x_2, y_2):
        self.points = (Point(x_1, y_1), Point(x_2, y_2))
        self.formula = 0
        super().__init__(x_1 + (x_1 + x_2) // 2,
                         y_1 + (y_1 + y_2) // 2)


class Area(Geometry):
    def __init__(self):
        super().__init__()


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
