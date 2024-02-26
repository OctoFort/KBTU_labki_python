string = input()
lowerSum = 0

lowerSum = sum(1 for i in string if i.islower())
upperSum = sum(1 for i in string if i.isupper())

print(f"lowercase: {lowerSum}")
print(f"uppercase: {upperSum}")
