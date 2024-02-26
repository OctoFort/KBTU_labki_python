letters = [chr(i) for i in range(65, 91)]


for i in letters:
    file = open(
        f"/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_6/dir-files/generatedFiles/gen1/{i}.txt",
        "w",
    )
    file.close()
