class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        return self.area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.area = length*width

def main():
    length = int(input("Length = "))
    width = int(input("Width = "))
    a = Rectangle(length, width)
    print(a.Area())

main()