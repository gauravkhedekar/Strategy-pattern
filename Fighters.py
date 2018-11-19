import style

class Fighter(object):
    def __init__(self, name=None , health=100 ):
        self.name = name
        self.health = health
        self.fighting_style = style.Style()

    def attack(self ,attacker ,  defender):
        self.fighting_style.attack(attacker ,defender)

    def defend(self ,attacker,  defender):
        self.fighting_style.defend(attacker , defender)


class AsianFighter(Fighter):
    def __init__(self ,  name=None , health=100 , fighting_style=None):
        super(AsianFighter , self).__init__(name , health)
        self.fighting_style = fighting_style

    def looks(self):
        print("{0.name} has asian look".format(self))

    def style(self):
        print("{0.name} has  {0.fighting_style} style".format(self))


class EuropeanFighter(Fighter):
    def __init__(self, name=None, health=100 , fighting_style=None):
        super(EuropeanFighter , self).__init__(name, health)
        self.fighting_style = fighting_style

    def looks(self):
        print("{0.name} has European look".format(self))

    def style(self):
        print("{0.name} has  {0.fighting_style} style".format(self))






