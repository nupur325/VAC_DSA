#return largest digit in a number
def returnLargestNumber():
    largest = 0
    while n>0:
        digit = n%10
        if digit>largest:
            largest=digit
        n//=10
    return largest