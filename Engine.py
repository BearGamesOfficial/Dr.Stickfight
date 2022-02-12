from math import sqrt

# If text of commit didn't saved - Last change is
# "Ended class Line; comapres for Areas"

# Next declared geometry properties


class Geometry:
    def __init__(self, x, y):
        self.center = (x, y)
        self.id = id(self)

    #def __str__(self): return f"Point with the center in ({self.center[0]}, {self.center[1]})"
    # Geometric shapes are the basis of the engine


class Point(Geometry):
    def __init__(self, x, y): super().__init__(x, y)

    def __add__(self, other): return Point(self.center[0] + other.center[0], self.center[1] + other.center[1])

    def __sub__(self, other): return Point(self.center[0] - other.center[0], self.center[1] - other.center[1])

    def __eq__(self, other): return self.center == other.center

    def __lt__(self, other): return self.center[1] < other.center[1]

    def __le__(self, other): return self.center[0] < self.center[0]

    def __ne__(self, other): return not (self == other)

    def __gt__(self, other): return not (self < other)

    def __ge__(self, other): return not (self <= other)

    def coord(self, x0=0, y0=0): return self - Point(x0, y0)
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
        else:
            raise TypeError("Geometry didn't detected")

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
        self.segments = list(segments)
        self.x = []
        self.y = [i.center[1] for j in self.segments for i in j.points if self.x.append(i.center[0]) is None]
        self.intersections = {}
        self.length = sum([sqrt((x.points[1].center[0] - x.points[0].center[0]) ** 2 + (
                x.points[1].center[1] - x.points[0].center[1]) ** 2) for x in self.segments])
        super().__init__(max(self.x) - min(self.x), max(self.y) - min(self.y))

    def __eq__(self, other):
        if other.__class__ is Point or other.__class__ is Segment:
            res = False
            # Go through segments list and checking with old method
            for i in self.segments:
                if i == other:
                    res = True
                    break
            return res
        elif other.__class__ is Line:
            res = False
            # Line is set of segments but __eq__ for Line and other Segments have been already described
            for i in other.segmets:
                if self == i:
                    res = True
            return res
        else:
            raise TypeError("Geometry didn't detected")

    def __add__(self, other):
        if other.__class__ is Segment:
            if other not in self.segments:
                self.segments.append(other)
        elif other.__class__ is Line:
            a = [0 for i in other.segments if i not in self.segments if self.segments.append(other) is None]
        else:
            raise TypeError(f"Line is set only of Segments, not {other.__class__}")

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

    def __str__(self): return f"Line from {str(self.segments[0].points[0])} to {str(self.segments[-1].points[1])} with \
{len(self.segments)} segments"

    def join(self):
        self.intersections = {}
        for ind, segm in enumerate(self.segments):
            for i in segm.intersections:
                self.intersections[(ind, i)] = segm.intersections[i]
        # Now self.intersections is looking like:
        # {
        #     (<index of segment in line (ind 0)>, <id of object which intersect this line (id A)>):
        #         <point 1>,
        #         <point 2>,
        #     (<ind 0>, <id B>):
        #         <point 1>,
        #     (<ind 1>, <id C>):
        #         <point 1>
        # }

    # Line is A line is a set of segments. The segments can be on the plane at any angles and the center of this line
    # is not necessarily on the line connecting its ends.


class Area(Geometry):
    def __init__(self, border=Line(Segment(0, 0, 0, 0)), area=0):
        self.x = []
        self.y = []
        self.intersections = {}
        self.inclusions = []
        self.overlays = {}
        self.border_length = 0
        self.border = border
        self.area = area
        self.area_locked = False
        self.length_locked = False
        super().__init__(border.center[0], border.center[1])

    def __eq__(self, other):
        if other.__class__ is Area:
            return self.area == other.area
        else:
            raise TypeError(f"Can't compare Area and {other.__class__}")
        # Slightly different comparison:
        # a == b compares areas of a and b;
        # a += b compares center points of a and b;
        # a -= b compares border length of a and b.

    def __iadd__(self, other):
        if other.__class__ is Area:
            return self.center == other.center
        else:
            raise TypeError(f"Can't compare Area and {other.__class__}")

    def __isub__(self, other):
        if other.__class__ is Area:
            return self.border_length == other.border_length
        else:
            raise TypeError(f"Can't compare Area and {other.__class__}")

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.area, self.center, self.border_length) < (other.area, other.center, other.border_length)

    def __le__(self, other):
        return (self.area, self.center, self.border_length) <= (other.area, other.center, other.border_length)

    def __gt__(self, other):
        return not ((self.area, self.center, self.border_length) < (other.area, other.center, other.border_length))

    def __ge__(self, other):
        return not ((self.area, self.center, self.border_length) <= (other.area, other.center, other.border_length))

    def __add__(self, other):
        if other.__class__ is Area:
            pass
        else:
            raise TypeError(f"Can't add {other.__class__} to Area")

    def __sub__(self, other):
        if other.__class__ is Area:
            pass
        else:
            raise TypeError(f"Can't sub {other.__class__} from Area")

    # 3 Ways to increase area:
    # 1) a * n - increases in y-axis;
    # 2) a *= n - increases in x-axis;
    # 3) a ** n = increases all axis

    def __mul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __pow__(self, power):
        return (self * sqrt(power)).__imul__(sqrt(power))

    # 4 Ways to decrease area:
    # 1) a / n - decreases in y-axis;
    # 2) a /= n - decreases in x-axis;
    # 3) a // n = decreases all axis;
    # 4) a % n = mod of a // n

    def __str__(self):
        return f"Line from {str(self.points[0])} to {str(self.points[-1])} with {len(self.points)} points"
    # A segment is a part of a straight line passing through 2 given points and bounded by them.


# Next declared properties of physic objects

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
segm2 = Segment(0, 0, 10, 5)
segm3 = Segment(0, 0, 10, 10)
segm4 = Segment(0, 0, 10, 0)
line = Line(segment, segm2, segm3)
if line == segm4:
    print("Ok")
else:
    print("blyat")
line.join()
