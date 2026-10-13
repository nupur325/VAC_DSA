def countPrime(n):
    count = 0
    sum = 1
    for i in range(2,n+1):
        prime = True
        for j in range(2,i):  #(2,int(i**0.5)+1) root logic
            if i % j == 0:
                sum = n//j +sum
                prime = False
                break
        if prime:
                count +=1
    return count
