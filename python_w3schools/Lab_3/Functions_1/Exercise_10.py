def unique(listik):
    new_listik = []
    for x in listik:
        if x not in new_listik:
            new_listik.append(x)
    return new_listik

def main():
    listik = [x for x in input().split()]
    print(unique(listik))
main()