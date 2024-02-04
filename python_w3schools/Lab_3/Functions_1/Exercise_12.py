def histogram(listik):
    for x in listik:
        print('*'*x)

def main():
    listik = [int(x) for x in input().split()]
    histogram(listik)
main()