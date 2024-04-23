str=input("Enter a palidrome ")

def check_palindrome(inp):
    rev = inp[::-1]

    if (inp == rev):
        print(f"{inp} this is a palindrome")
    else:
        print(f"{inp} is not a palidrome")

check_palindrome(str)