class Eater(object):
    def __init__(self,data):
        self.name = data["name"]
        self.score = data['chickenwings']*5 + data['hamburgers']*3 + data['hotdogs']*2

def scoreboard(who_ate_what):
    eaters = []
    for eater in who_ate_what:
        eater = Eater(eater)
        eaters.append({'name':eater.name, 'score':eater.score})
    eaters.sort(key = lambda k: k['score'], reverse = True)
    for i in range(len(eaters)-1):
        if (eaters[i]["score"] == eaters[i+1]["score"]) and (eaters[i]["name"] > eaters[i+1]["name"]):
            eaters[i+1], eaters[i]  = eaters[i], eaters[i+1]

    return eaters

scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},{"name": "Habanero Hillary", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},{"name": "Joey Jaws", "chickenwings": 8, "hamburgers"\
: 8, "hotdogs": 15},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}])
