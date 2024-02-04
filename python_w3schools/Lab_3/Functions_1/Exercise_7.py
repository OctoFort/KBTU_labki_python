def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True

    return False

def main():
    listik = [int(x) for x in input().split()]
    print(has_33(listik))

main()