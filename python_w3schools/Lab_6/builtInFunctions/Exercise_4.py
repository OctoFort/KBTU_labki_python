from time import sleep

number = int(input())
sleepTime = int(input())
sleep(sleepTime / 1000)
print(f"Square root of {number} after {sleepTime} miliseconds is {number**0.5}")
