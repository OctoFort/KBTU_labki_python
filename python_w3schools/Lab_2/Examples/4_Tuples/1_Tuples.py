thistuple = ("apple", "banana", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry", "apple", "cherry") #duplicates
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Is a tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#count()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)