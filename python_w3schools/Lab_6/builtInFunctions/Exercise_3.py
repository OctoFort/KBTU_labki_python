string = input()

(
    print("Is palindrom")
    if string.lower() == "".join([i for i in reversed(string)]).lower()
    else print("Is not palindrom")
)
