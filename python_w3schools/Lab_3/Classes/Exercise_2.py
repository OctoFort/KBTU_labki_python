class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = length**2

def main():
    length = int(input("Length = "))
    a = Square(length)
    print(a.Area())

main()