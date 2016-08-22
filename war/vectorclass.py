import math



class Vector:
    def __init__(self, array):
        self.array = array

    def check_length(self,other):
        if len(self.array) == len(other.array):
            pass
        else:
            raise ValueError("They are not the same length!")

    def add(self, other):
        self.check_length(other)
        vectorSum = []
        for i in range(0,len(self.array)):
            vectorSum.append(self.array[i] + other.array[i])
        return Vector(vectorSum)

    def subtract(self,other):
        self.check_length(other)
        vectorDiff = []
        for i in range(0,len(self.array)):
            vectorDiff.append(self.array[i] - other.array[i])
        return Vector(vectorDiff)

    def dot(self, other):
        self.check_length(other)
        vectorDot = 0
        for i in range(0,len(self.array)):
            vectorDot += self.array[i]*other.array[i]
        return vectorDot

    def norm(self):
        n = 0
        for i in self.array:
            n += i**2
        return math.sqrt(n)

    def toString(self):
        tup = ()
        for i in self.array:
            tup += (i,)
        return str(tup)

    def __str__(self):
        tup = ()
        for i in self.array:
            tup += (i,)
        return str(tup)

    def equal(self,other):
        if self.array == other.array:
            return True
        return False

a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([1,2,3])

print a.add(b).array
print a.subtract(b).array
print a.dot(b)
print a.norm()
print str(a)
print a.equal(c)
