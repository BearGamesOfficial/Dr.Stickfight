class Geometry:
    def __init__(self, x, y):
        self.center = (x, y)

    def __str__(self):
        return f"Point with the center in ({self.center[0]}, \
{self.center[1]})"
    # Geometric shapes are the basis of the engine


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

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.center[1] < other.center[1]

    def __le__(self, other):
        return self.center[0] < self.center[0]

    def __gt__(self, other):
        return not (self < other)

    def __ge__(self, other):
        return not (self <= other)

    def coord(self, x0=0, y0=0):
        return self - Point(x0, y0)
    # Point is basic element of geometry. It has only center.


class Segment(Geometry):
    def __init__(self, x_1, y_1, x_2, y_2):
        self.points = [Point(x_1, y_1), Point(x_2, y_2)]
        super().__init__(x_1 + (x_1 + x_2) // 2,
                         y_1 + (y_1 + y_2) // 2)

    def __eq__(self, other):
        if other.__class__ is Point:
            # Если x точки м/у минимальным x и максимальным =>
            # проверять соответствие формуле, где x = point.center[0];
            # y = point.center[1]. х используется в формуле,
            # сравнивать нужно по y.
            x = 1
            formula = (self.points[0].center[1] -
                       self.points[1].center[1]) / \
                      (self.points[0].center[0] -
                       self.points[1].center[0]) * x + \
                      self.points[1].center[1] - \
                      (self.points[0].center[1] -
                       self.points[1].center[1]) / \
                      (self.points[0].center[0] -
                       self.points[1].center[0]) * \
                      self.points[1].center[0]
            # This construction computes Y of the function for a
            # given X
            print(formula)

    def __str__(self):

    # A segment is a part of a straight line passing through 2 given
    # points and bounded by them.


class Line(Geometry):
    def __init__(self, *segments):
        pass
        super().__init__(None, None)
    # Line is A line is a set of segments. The segments can be on the
    # plane at any angles and the center of this line is not
    # necessarily on the line connecting its ends.


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


point = Point(0, 2)
line = Segment(0, 0, 10, 20)
print(line == point)
