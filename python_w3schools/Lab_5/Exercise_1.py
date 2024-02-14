import re

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_1.txt') as file:
    for line in file:
        splitline = line.split()
        for i in splitline:         
            reslipr = re.match('ab*', i)
            if reslipr:
                result.append(reslipr.string)


for i in result:
    print(i, end=' ')