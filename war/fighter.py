"""
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious.
Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0.
You can mutate the Fighter objects

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

"""
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self. damage_per_attack = damage_per_attack

    def lose_health(self,damage):
        self.health -= damage

def declare_winner(fighter1, fighter2, first_attacker):
    attacker = first_attacker
    while fighter1.health > 0 and fighter2.health > 0:
        print fighter1.name + " - " + str(fighter1.health)
        print fighter2.name + " - " + str(fighter2.health)
        print attacker + " attacks!\n"
        raw_input()
        if attacker == fighter1.name:
            fighter2.lose_health(fighter1.damage_per_attack)
            attacker = fighter2.name
        else:
            fighter1.lose_health(fighter2.damage_per_attack)
            attacker = fighter1.name
    if fighter1.health > fighter2.health:
        return fighter1.name
    return fighter2.name
