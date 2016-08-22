import math

def isPrime(number):
    if number%2 == 0 and number > 2:
        return False
    for x in range (3,int(math.sqrt(number))+1,2):
        if number%x == 0:
            return False
    return True

class Primes:
    def __init__(self):
        self.first = None


    global isPrime

    @classmethod
    def first(self, x):
        primes = [2]
        a = 3
        while len(primes) < x:
            if isPrime(a):
                primes.append(a)
            a += 2
        return primes

    def last(self,y):
        return self.first(x)[-y]

#    First = first(x)
#    def last(self,x):
#        return self.primes[-x:]

print Primes.first(5)

print Primes.first(5).last(2)
