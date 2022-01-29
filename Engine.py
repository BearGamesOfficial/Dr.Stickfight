from math import sqrt


class Geometry:
    def __init__(self, x, y):
        self.center = (x, y)
        self.id = id(self)

    def __str__(self):
        return f"Point with the center in ({self.center[0]}, {self.center[1]})"
    # Geometric shapes are the basis of the engine


class Point(Geometry):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __eq__(self, other):
        return self.center == other.center

    def __add__(self, other):
        return Point(self.center[0] + other.center[0], self.center[1] + other.center[1])

    def __sub__(self, other):
        return Point(self.center[0] - other.center[0], self.center[1] - other.center[1])

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
        self.x = []
        self.y = [i.center[1] for i in self.points if self.x.append(i.center[0]) is None]
        self.intersections = {}
        self.length = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        super().__init__(x_1 + (x_1 + x_2) // 2, y_1 + (y_1 + y_2) // 2)

    def formula(self, x):
        return (self.points[0].center[1] - self.points[1].center[1]) / \
               (self.points[0].center[0] - self.points[1].center[0]) * x + self.points[1].center[1] - \
               (self.points[0].center[1] - self.points[1].center[1]) / \
               (self.points[0].center[0] - self.points[1].center[0]) * self.points[1].center[0]
        # This construction computes Y of the function for a given X

    def __eq__(self, other):
        if other.__class__ is Point:
            # Determining the coordinates of a point
            x_p, y_p = other.center
            # Checking whether the point falls into the dimensions of the segment
            if (min(self.x) <= x_p <= max(self.x)) and (min(self.y) <= y_p <= max(self.y)):
                return self.formula(x_p) == y_p
            else:
                return False
        elif other.__class__ is Segment:
            result, x_range = False, (0, 0)
            # Finding intersections of the segments in X-axis
            if not (max(self.x) < min(other.x) or min(self.x) > max(other.x)):
                if min(self.x) < min(other.x):
                    x_range = (min(other.x), max(self.x))
                else:
                    x_range = (min(self.x), max(other.x))
            # Running through the intersection of the segments and look for a common point
            for x in range(x_range[0], x_range[1]):
                if self.formula(x) == other.formula(x):
                    result = True
                    self.intersections[other.id] = Point(x, self.formula(x))
                    break
            return result

    def __add__(self, other):
        return Line(self, other)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __gt__(self, other):
        return not (self < other)

    def __ge__(self, other):
        return not (self <= other)

    def __str__(self):
        return f"Line from {str(self.points[0])} to {str(self.points[-1])} with {len(self.points)} points"
    # A segment is a part of a straight line passing through 2 given points and bounded by them.


class Line(Geometry):
    def __init__(self, *segments):
        self.segments = segments
        self.x = []
        self.y = [i.center[1] for j in self.segments for i in j.points if self.x.append(i.center[0]) is None]
        self.intersections = {}
        self.length = sum([sqrt((x.points[1].center[0] - x.points[0].center[0]) ** 2 + (
                x.points[1].center[1] - x.points[0].center[1]) ** 2) for x in self.segments])
        super().__init__(max(self.x) - min(self.x), max(self.y) - min(self.y))

    def __str__(self):
        return f"Line from {str(self.segments[0].points[0])} to {str(self.segments[-1].points[1])} with \
{len(self.segments)} segments"
    # Line is A line is a set of segments. The segments can be on the plane at any angles and the center of this line
    # is not necessarily on the line connecting its ends.


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


segment = Segment(0, 0, 10, 20)
segm2 = Segment(1, 0, 4, 12)
line = Line(segment, segm2)
