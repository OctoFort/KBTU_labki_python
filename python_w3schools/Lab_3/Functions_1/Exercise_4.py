from math import sqrt

def filter_prime(listik):
    newlistik = []

    for i in listik:
        boolean = True
        if i <= 1: continue
        for x in range(2, i):

            if i%x == 0:
                boolean = False
                break
        
        if boolean:
            newlistik.append(i)
        else:
            continue


    return newlistik



def main():
 
    listik = [int(x) for x in input().split()]

    print(filter_prime(listik))


main()