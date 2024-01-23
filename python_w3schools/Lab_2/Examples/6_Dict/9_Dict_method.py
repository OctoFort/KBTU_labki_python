#fromkeys()

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

xx = ('key1', 'key2', 'key3')
yy = ('test1', 'test2', "test")

newdict = dict.fromkeys(xx, yy)

print(newdict)