def reverser(text):
    text.reverse()
    return text

def main():
    listik = [x for x in input().split()]

    [print(x, end=' ') for x in reverser(listik)]

main()

