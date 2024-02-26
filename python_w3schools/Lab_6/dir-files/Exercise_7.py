with open(
    "/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_6/dir-files/copying/start.txt"
) as start:
    with open(
        "/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_6/dir-files/copying/end.txt",
        "w",
    ) as end:
        end.writelines(start)
