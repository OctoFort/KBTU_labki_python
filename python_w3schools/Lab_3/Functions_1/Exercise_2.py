def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C

def main():
    F = int(input("Input Fahrenheit: "))
    print(F_to_C(F))

main()