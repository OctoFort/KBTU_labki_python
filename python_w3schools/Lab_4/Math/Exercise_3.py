import math

number_of_sides = int(input("Input number of sides: "))
length_of_side = float(input("Input length of side: "))

if number_of_sides > 2 and length_of_side > 0:
    area = (number_of_sides * length_of_side**2) / (4 * math.tan(math.pi / number_of_sides))
    print(round(area, 2))

else:
    print("Doesn't exist")