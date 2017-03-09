class Point:
    "create a point object in XY plane"
    def __init__(self,x=0,y=0):
        "initialize point coordinate to (x,y)"
        self.x = x
        self.y = y

    def DistanceFromOrigin(self):
        "return float"
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return "({0}, {1})".format(self.x,self.y)

    def MidPoint(self,pointB):
        "return midpoint's coordinate"
        return Point((self.x+pointB.x)/2, (self.y+pointB.y)/2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        "dot product of two points"
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        "scalar multiplication"
        # right operand is self, left operand is other
        return Point(other*self.x, other* self.y)

if __name__ == "__main__":
    print(callable(Point))
    print(dir(Point))
    print(Point().__class__ is Point)
    print(Point.__class__)
    print(Point.__name__)
    PP = Point
    a = PP(3,4)
    print(a.DistanceFromOrigin())
    print(a)
    print(a.MidPoint(Point()))
    a = Point(1,2)
    b = Point(1,2)
    print(a == b) # shallow equality test, false if they are not alias
    print([1,2] == [1,2]) # but that's only for user defined object
    print(a+b)
    print(a*b)
    print(10*a)
