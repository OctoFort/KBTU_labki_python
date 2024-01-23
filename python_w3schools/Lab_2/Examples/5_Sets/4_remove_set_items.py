#remove()

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #if no "banana" raise error

print(thisset)


#discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #if no "banana" will not raise error

print(thisset)


#pop() delete random

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



#clear()

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



#del

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)