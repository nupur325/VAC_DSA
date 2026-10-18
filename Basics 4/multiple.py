#nearest multiple of 10
def multiple(s):
    n = n%10
    rem = n%10
    if rem <=5 :
        return n-rem
    else:
        return n + (10 - rem)