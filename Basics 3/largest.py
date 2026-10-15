def largest(n):
    digit = 0
    largest = 0
    while n>0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n//=10
    return largest