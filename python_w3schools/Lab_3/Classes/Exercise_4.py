from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("X: ", self.x, "\t", "Y: ", self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, point):
        print(sqrt( (point.x - self.x)**2 + (point.y - self.y )**2) )

def main():
    point1 = Point(1, 2)
    point1.move(-1, -4)
    point2 = Point(0, 1)


    point1.show()
    point1.dist(point2)
main()