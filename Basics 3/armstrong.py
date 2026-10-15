def armstrong(n):
    original = n
    total = 0
    count = len(str(n))
    while n>0:
        digit = n % 10
        total += digit ** count
        n//=10
    return total == original