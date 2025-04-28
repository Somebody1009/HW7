import math

class Figure:
    def dimension(self):
        raise NotImplementedError()

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError()

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        s = (self.a + self.b + self.c + self.d) / 2
        height = (math.sqrt((s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)) * 2) / (self.a + self.b)
        return ((self.a + self.b) / 2) * height

    def volume(self):
        return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r * self.r

    def volume(self):
        return self.square()

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r * self.r

    def volume(self):
        return (4/3) * math.pi * self.r ** 3

class Cone(Figure):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def dimension(self):
        return 3

    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * l

    def squareBase(self):
        return math.pi * self.r ** 2

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * math.pi * self.r ** 2 * self.h

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return 3

    def squareSurface(self):
        base_area = super().square()
        side_area = (3 * (self.a * math.sqrt((self.h ** 2) + ((self.a * math.sqrt(3)) / 6) ** 2))) / 2
        return side_area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * super().square() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimension(self):
        return 3

    def squareSurface(self):
        return self.a * math.sqrt((self.b / 2) ** 2 + self.h ** 2) + self.b * math.sqrt((self.a / 2) ** 2 + self.h ** 2)

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * super().square() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def squareSurface(self):
        return 2 * (self.a*self.b + self.b*self.c + self.a*self.c)

    def height(self):
        return self.c

    def volume(self):
        return self.a * self.b * self.c

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return 3

    def squareSurface(self):
        return (self.a + self.b + self.c) * self.h

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return super().square() * self.h
