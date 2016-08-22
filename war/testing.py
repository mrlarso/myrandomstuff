def yo(name = "mick"):
        def hi():
            return "you mick"
        def sup():
            return "you aint mick"
        if name == "mick":
            return hi
        else:
            return sup

def whatup():
    print "Hi Mick"
"""
def my_dec(func):
    print "INB4"
    print func()
    print "after function"
"""
def my_other_dec(func):
    def my_dec():
        print "INB4"
        func()
        print "after function"
    return my_dec

yo = my_other_dec(whatup)

print yo()
#whatup = my_other_dec(whatup)

#print whatup()
