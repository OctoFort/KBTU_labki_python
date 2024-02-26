count = 0
with open(
    "/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_6/dir-files/test1/text1.txt"
) as file:
    for line in file:
        count += 1
print(f"{count} lines")
