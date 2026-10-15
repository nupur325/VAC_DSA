def palindrome(n):
    digit = 0
    original = n
    rev = 0
    while n>0:
        digit = n % 10
        rev = rev * 10 + digit
        n//=10
    return original == rev