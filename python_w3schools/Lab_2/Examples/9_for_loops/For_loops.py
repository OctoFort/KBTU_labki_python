#loop list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#loop string
for x in "banana":
    print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#if
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


#range()
for x in range(6):  # 0 1 2 3 4 5
    print(x)

for x in range(2, 6): # 2 3 4 5 
    print(x)

for x in range(2, 30, 3): #2 5 8 11...
    print(x)

#else
    
for x in range(6):
    print(x)
else:
    print("Finally finished!")