from math import sqrt
from math import pi
import random

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


def F_to_C(F):
    C = (5 / 9) * (F - 32)
    return C


def solve(numheads, numlegs):
    rabbit = (numlegs-numheads*2)/2
    chicken = numheads-rabbit
    print(f"Rabbits: {int(rabbit)}")
    print(f"Chicken: {int(chicken)}")


def filter_prime(listik):
    newlistik = []

    for i in listik:
        boolka = False
        count = 0
        for x in range(1,i+1):
            if i/x == int(i/x):
                count+=1
            if count > 2:
                boolka = True
                break

        
        if boolka:
            continue
        else:
            newlistik.append(i)
            

    return newlistik


def reverser(text):
    text.reverse()
    return text


def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True

    return False


def spy_game(nums):
    count = 0
    for x in nums:
        if x in [1, 2, 3, 4, 5, 6, 8, 9]:
            continue
        elif x == 0 and count == 0 or count == 1:
            count+=1
        elif x == 7 and count == 2:
            return True
    return False


def volume_sphere(r):
    return (4/3)*pi*r**3


def unique(listik):
    new_listik = []
    for x in listik:
        if x not in new_listik:
            new_listik.append(x)
    return new_listik



def histogram(listik):
    for x in listik:
        print('*'*x)


def Guess_the_number():
    count= 0
    name = str(input("Hello what is your name?\n"))
    print(f"Well, {name}, I am thinking of a number between 1 and 20")
    rand = random.randint(1, 20)

    while True:
        print("Take a guess.")
        ans = int(input())
        count+=1
        if ans < rand:
            print("Your guess is too low.")
        elif ans == rand:
            break
        elif ans > rand:
            print("Your guess is too high.")
    print(f"Good job, {name}! You guessed my number in {count} guesses!")
