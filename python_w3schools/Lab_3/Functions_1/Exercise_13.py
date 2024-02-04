import random
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


Guess_the_number()