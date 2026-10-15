#find largest digit in a number
def largest(n):
    digit = 0
    large = 0
    while n>0:
        digit = n % 10
        if digit > large:
            large = digit
        n//=10
    return large