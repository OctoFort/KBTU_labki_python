import re

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_4.txt') as file:
    for line in file:
        splitline = line.split()
        for string in splitline:
            text = re.match('[A-Z][a-z]+$' ,string)
            if text:                    
                result.append(text.string)

for i in result:
    print(i)