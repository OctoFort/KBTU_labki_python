# gen = (num**2 for num in range(1, a+1))

def genik(n):
    for i in range(1,n+1):
        yield i**2

a = int(input("squares of numbers up to: "))

gen = genik(a)

for i in gen:
    print(i)