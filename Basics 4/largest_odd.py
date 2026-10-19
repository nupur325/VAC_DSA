#largest odd num in a list ... 
def largestOdd(s:str)->str:
    n = int(s)
    while n>0:
        if n%2!=0:
            return n
        n//=10
    return ""