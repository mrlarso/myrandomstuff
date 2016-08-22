import math

def isPrime(number):
    if number%2 == 0 and number > 2:
        return False
    for x in range (3,int(math.sqrt(number))+1,2):
        if number%x == 0:
            return False
    return True

class Primes(list):
    def __init__(self, primesList = []):
        super(Primes,self).__init__(primesList)
        self.primes = primesList

    global isPrime

    @classmethod
    def first(self, x):
        primes = [2]
        a = 3
        while len(primes) < x:
            if isPrime(a):
                primes.append(a)
            a += 2
        return Primes(primes)


    def last(self,x):
        return self[-x:]

print Primes.first(100)[99]
