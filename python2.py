def pal(str):
    rev = ""
    for ch in str:
        rev = ch + rev
    return (rev)
if __name__ == '__main__':
    str = input("Enter a string : ")
    rev = pal(str)
    if rev == str:
        print("Palindrome")
    else:
        print("Not Palindrome")
