def palindrome(string):
    rstring = string[::-1]

    if string == rstring:
        return True
    else:
        return False

def main():
    string = str(input())
    print(palindrome(string))

main()