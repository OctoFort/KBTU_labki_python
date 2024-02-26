myList = [i for i in input().split()]

with open(
    "/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_6/dir-files/test1/text2.txt",
    "w",
) as file:
    for i in myList:
        file.writelines(i + "\n")
