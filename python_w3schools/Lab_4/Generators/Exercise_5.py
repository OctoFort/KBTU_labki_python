def genik(a):
    for i in range(a, -1, -1):
        yield i

a = int(input("input: "))

for i in genik(a):
    print(i)