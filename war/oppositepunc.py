def group_check(s):
    # Get list of matching punctations and separate them from the rest of the characters
    opposites = {'{':'}','[':']','(':')',')':'(',']':'[','}':'{'}
    s = "".join([x if x in "[{()}]" else "" for x in s])
    print s
    raw_input()
    for x in s:
        print x
        print opposites[x]
        raw_input()
        if opposites[x] == s[s.index(x)+1]:
            s = s[:s.index(x)] + s[s.index(x) + 2:]
        print s
        raw_input()


    #    if opposites[s[i]] != s[-(i+1)] and opposites[s[i]] != s[i+1]:
    #        return False
    return True

print group_check("this is (just) a [Test]")
