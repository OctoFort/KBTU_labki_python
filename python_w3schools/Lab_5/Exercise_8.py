import re

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_8.txt') as file:
    for line in file:

        text = re.findall('[A-Z][a-z]*', line)
        result.append(text)

for i in result:
    print(i)