def outside(x = 5):
    def printHam():
        print x
    return printHam

myfunc = outside(7)

myfunc()
