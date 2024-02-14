import re

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_6.txt') as file:
    for line in file:
        text = re.sub('\s|,|\.', ':', line)
        if text:                    
            result.append(text)

for i in result:
    print(i)