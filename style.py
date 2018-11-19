class Style(object):
    def attack(self , opponent):
        pass

    def defend(self , defend):
        pass

class Kunfu(Style):
    def __init__(self):
        super(Kunfu ,self).__init__()


    def attack(self ,attacker, defender):
        print("{0.name} attacking {1.name} in kunfu style".format(attacker , defender))

    def defend(self , attacker , defender):
        print("{0.name} is defending {1.name} in kunfu style".format(attacker , defender))


class Judo(Style):
    def __init__(self):
        super(Judo, self).__init__()

    def attack(self, attacker, defender):
        print("{0.name} attacking {1.name} in judo style".format(attacker, defender))

    def defend(self, attacker, defender):
        print("{0.name} is defending {1.name} in judo style".format(attacker, defender))


class Karate(Style):
    def __init__(self):
        super(Karate, self).__init__()

    def attack(self, attacker, defender):
        print("{0.name} attacking {1.name} in karate style".format(attacker, defender))

    def defend(self, attacker, defender):
        print("{0.name} is defending {1.name} in karate style".format(attacker, defender))

class Muythai(Style):
    def __init__(self):
        super(Muythai, self).__init__()

    def attack(self, attacker, defender):
        print("{0.name} attacking {1.name} in muythai style ".format(attacker, defender))

    def defend(self, attacker, defender):
        print("{0.name} is defending {1.name} in muythai style ".format(attacker, defender))