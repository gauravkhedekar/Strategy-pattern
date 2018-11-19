import style
import Fighters

fighter1 = Fighters.AsianFighter(name="Raj" , fighting_style = style.Kunfu())
fighter2 = Fighters.EuropeanFighter(name="mcgregor" , fighting_style = style.Judo())

# AsianFighter.looks(fighter1)
# main.EuropeanFighter.looks(fighter2)
Fighters.AsianFighter.style(fighter1)
Fighters.EuropeanFighter.style(fighter2)

fighter1.attack(fighter1 , fighter2)
fighter2.defend(fighter1 , fighter2)
fighter2.attack(fighter2 , fighter1)
fighter1.defend(fighter1 , fighter2)

fighter1.fighting_style = style.Karate()
# print(Fighters.fighter1.fighting_style)
print("changing fighting style of raj")
Fighters.AsianFighter.style(fighter1)
fighter1.attack(fighter1,fighter2)