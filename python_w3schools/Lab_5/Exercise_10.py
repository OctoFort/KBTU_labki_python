import re

def lowerr(match):
    return match.group(1)+"_"+ match.group(2).lower() 

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_9.txt') as file:
    for line in file:

        text = re.sub('(.)([A-Z])',lowerr,line)
        result.append(text)

for i in result:
    print(i)

