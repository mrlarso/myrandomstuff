def goodVsEvil(good, evil):
    goodValue, evilValue = [1,2,3,3,4,10], [1,2,2,2,3,5,10]
    goodTotal, evilTotal = 0, 0
    for i in range(0,6):
        goodTotal += int(good.split()[i])*goodValue[i]
    for i in range(0,7):
        evilTotal += int(evil.split()[i])*evilValue[i]
    if goodTotal > evilTotal:
        return "Battle Result: Good triumphs over Evil"
    elif evilTotal > goodTotal:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
