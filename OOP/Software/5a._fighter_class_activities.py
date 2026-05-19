import random

#3. Implement the game with a private __health attribute

class Fighter:
    def __init__(self,name,starting_health,weapon,shield):
        self.name = name
        self.__health = starting_health
        self.shield = shield
        self.weapon = weapon


    def report(self):
        print(self.name+' health: '+str(self.__health))

    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
you = Fighter('You', 100,60,20)
troll = Fighter('Troll',200,30,10)


you.report()
troll.report()
print('You attack the troll...')
troll.__health -= you.random_attack()
troll.report()
print('The troll attacks you...')
you.__health -= troll.random_attack()
you.report()
#2. Test the game 