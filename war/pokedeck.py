
class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype
        if self.pkmntype == "water":
            self.typedesc = "wet"
        else:
            self.typedesc = self.pkmntype + "y"
        if self.level <= 20:
            self.strength = 'weak'
        elif self.level > 20 and self.level <= 50:
            self.strength = 'fair'
        else:
            self.strength = 'strong'

    def info(self):
        return "%s, a %s and %s Pokemon." %(self.name, self.typedesc, self.strength)

s = PokeScan('Squirtle', 21, 'water')
c = PokeScan('Charmander', 55, 'fire')

print c.info()
print s.info()
