spoken    = lambda greeting: greeting
shouted   = lambda greeting: greeting[:-1].upper() + '!'
whispered = lambda greeting: greeting.lower()

greet = lambda style, msg:  style(msg)

print greet(spoken,'Hello.')
print greet(shouted,'Hello.')
print greet(whispered,'Hello.')
