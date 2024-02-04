from math import pi

def volume_sphere(r):
    return (4/3)*pi*r**3

def main():
    r = float(input())
    print(volume_sphere(r))

main()