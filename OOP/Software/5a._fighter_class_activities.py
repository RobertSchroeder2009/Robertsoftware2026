import random

#3. Implement the game with a private __health attribute

class Fighter:
    def __init__(self,name,starting_health,weapon,shield):
        self.name = name
        self.health = starting_health
        self.shield = shield
        self.weapon = weapon


    def report(self):
        print(self.name+' health: '+str(self.health))

    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
you = Fighter('You', 100,60,20)
troll = Fighter('Troll',200,30,10)


you.report()
troll.report()
#1. Create a loop which simulates a fight and declares a winner
print('You attack the troll')
troll.health -= you.random_attack()
troll.report()

#2. Test the game 