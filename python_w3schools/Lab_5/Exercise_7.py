import re

def upperr(match):
    return match.group(2).upper()

result = []

with open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_5/txt/txt_7.txt') as file:
    for line in file:

        text = re.sub('(_)(.)', upperr, line)
        if text:                    
            result.append(text)

for i in result:
    print(i)