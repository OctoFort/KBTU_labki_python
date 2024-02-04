def spy_game(nums):
    count = 0
    for x in nums:
        if x in [1, 2, 3, 4, 5, 6, 8, 9]:
            continue
        elif x == 0 and count == 0 or count == 1:
            count+=1
        elif x == 7 and count == 2:
            return True
    return False

def main():
    nums = [int(x) for x in input().split()]
    print(nums)
    print(spy_game(nums))

main()