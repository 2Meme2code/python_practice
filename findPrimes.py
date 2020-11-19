from datetime import datetime
import math

def findPrimes(n):
    primes = [2]
    for num in range(3, n, 2):
        isprime = 1
        up = math.sqrt(num)
        for i in primes[1:]:
            if num % i == 0 or i > up :
                isprime = 0
                break
            
        if isprime == 1:
            primes.append(num)
    return primes


def perf(n):
    dt1 = datetime.now()
    #dt.microsecond
    num = findPrimes(n)
    dt2 = datetime.now()
    delta = dt2 - dt1

    print("2...", n, num)
    print (delta)
    
