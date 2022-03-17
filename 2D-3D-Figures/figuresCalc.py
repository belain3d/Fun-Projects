# Calculation of basic 2D and 3D figures
# Made by belain3d. Git Repo on https://github.com/belain3d/Fun-Projects #
import math

def squareroot(a):
    return a**0.5

# ---------------------------------------------- 2D Figures ---------------------------------------------- #

class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Area(self):
        return self.a*self.b

    def Perimeter(self):
        return 2*(self.a+self.b)

class quadrant:
    def __init__(self, a):
        self.a = a
    
    def Area(self):
        return self.a*self.a

    def Perimeter(self):
        return 4*self.a

    def Diagonal(self):
        return squareroot(self.a**2+self.a**2)

class triangle:
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.h = height

    def Area(self):
        return (self.a*self.h)/2
    
    def Perimeter(self):
        return self.a+self.b+self.c

class righttriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Area(self):
        return (self.a*self.b)/2

    def Perimeter(self):
        return self.a+self.b+self.c

class circle:
    def __init__(self, radius):
        self.r = radius

    def Area(self):
        return math.pi*self.r**2

    def Perimeter(self):
        return 2*math.pi*self.r

    def Diameter(self):
        return 2*self.r

# ---------------------------------------------- 3D Figures ---------------------------------------------- #

class cuboid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Volume(self):
        return self.a*self.b*self.c

    def Face(self):
        return 2*((self.a*self.b)+(self.a*self.c)+(self.b*self.c))

    def Diagonal(self):
        return squareroot((self.a**2)+(self.b**2)+(self.c**2))

class cylinder:
    def __init__(self, height, radius, diameter):
        self.height = height
        self.radius = radius
        self.diameter = diameter

    def Volume(self):
        return math.pi*self.radius**2*self.height

    def Base(self):
        return math.pi*self.radius**2

    def Wall(self):
        return 2*math.pi*self.radius*self.height 