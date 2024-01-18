#capitalize()

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

txt = "python is FUN!"

x = txt.capitalize()

print (x)

txt = "36 is my age."

x = txt.capitalize()

print (x)

#casefold()

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

#center()

txt = "banana"

x = txt.center(20)

print(x)

txt = "banana"

x = txt.center(20, "O")

print(x)

#count()

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)

#endswith()

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

#expandtabs()

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#format()

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#find()

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#index()

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#join()

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

#replace()

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

#split()

txt = "welcome to the jungle"

x = txt.split()

print(x)

#swapcase()

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)