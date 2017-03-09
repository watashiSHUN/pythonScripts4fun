from point import Point

class Rectangle:
    "create a rectangle (vertically/horizontally oriented) in XY plane"
    def __init__(self, leftCorner = Point(), width = 0, height = 0):
        self.leftCorner = leftCorner
        self.width = width
        self.height = height

    def __str__(self):
        return "({0}, {1}, {2})".format(self.leftCorner, self.width, self.height)

    def grow(self, deltaWidth, deltaHeight):
        "grow or shrink this rectangle by delta"
        self.width += deltaWidth
        self.height += deltaHeight

    def moveTo(self, leftCorner):
        "move the left corner of this rectangle to a new point"
        self.leftCorner = leftCorner

if __name__ == "__main__":
    rec = Rectangle(width = 10, height = 10)
    print(rec)
    rec.grow(5,10)
    print(rec)
    rec.moveTo(Point(1,-1))
    print(rec)
