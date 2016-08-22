def title_case(string, exceptions = ""):
    words = string.split()
    newstring = ""
    for i in range(len(words)):
        if i == 0 or words[i].lower() not in exceptions.lower()split():
            newstring += words[i].title() + " "
        else:
            newstring += words[i].lower() + " "
    return newstring[:-1]
print title_case('a clash of KINGS', 'a an the of')
