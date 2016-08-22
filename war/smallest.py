def smallest(n):
    sn = str(n)
    smallest = 10
    for i in range(1,len(sn)):
        if int(sn[i]) < smallest:
            smallest = int(sn[i])
            index = i
    if smallest < int(sn[0]):
        newindex = 0
        newn = int(sn[index] + sn[:index]+ sn[index+1:])
    else:
        newindex = 1
        newn = int(sn[:1] + sn[1:index] + sn[:index]+ sn[index+1:])
    return [newn,index,newindex]

for i in (261235, 209917, 285365, 269045, 296837):
    print smallest(i)
