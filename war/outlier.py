def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i%2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(odds) == 1:
        return odds[0]
    return evens[0]

def find_outlierb(integers):
    evens = [x for x in integers if x%2 == 0]
    odds = [x for x in integers if x%2 != 0]
    if len(odds) == 1:
        return odds[0]
    return evens[0]


print find_outlierb([2,6,8,10,3])
print find_outlierb([2, 4, 0, 100, 4, 11, 2602, 36])
print find_outlierb([160, 3, 1719, 19, 11, 13, -21])
