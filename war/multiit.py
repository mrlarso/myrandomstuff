def multiiter(*args):
    iterator = []
    if len(args) == 1:
        for i in range(args[0]):
            iterator.append((i,))
    else:
        for i in range (a,len(args)):
            for x in range(args[0]):
                for y in range(args[i]):
                    iterator.append((x,y))

    return iterator

for a in (0,1):
    print multiiter(a)

print multiiter(2,3)
print multiiter(2,3,4)
