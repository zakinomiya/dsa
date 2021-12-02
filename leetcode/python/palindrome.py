def isPalindrome(num) -> bool:
    if num < 0:
        return False

    strnum = str(num)
    r = ""
    for s in reversed(strnum):
        r += s

    return r == str(num)


if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(1221))
    print(isPalindrome(12))
