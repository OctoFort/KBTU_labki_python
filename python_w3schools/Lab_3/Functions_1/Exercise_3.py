def solve(numheads, numlegs):
    rabbit = (numlegs-numheads*2)/2
    chicken = numheads-rabbit
    print(f"Rabbits: {int(rabbit)}")
    print(f"Chicken: {int(chicken)}")

def main():
    numheads = int(input("amount of heads: "))
    numlegs = int(input("amount of legs: "))
    solve(numheads, numlegs)

main()