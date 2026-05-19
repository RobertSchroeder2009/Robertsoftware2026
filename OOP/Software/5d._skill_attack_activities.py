#Learning Intentions
#1. Create a skill attack method
#2. Use the time library to set up a timing measure (skill factor)
#3. Have the skill increase or decrease the final attack value

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+"'s "+ ' health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power


    def skill_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in the exactly',target,'seconds')
        time.sleep(1)
        print('Ready...')
        time.sleep(1)
        tic = time.time()
        if target > 5:
            print(6)
            time.sleep(1)
            print('')
        if target == 5:
            print('')
            time.sleep(1)
        if target > 3:
            print(4)
            time.sleep(1)
            print('')
        if target == 3:
            print('')
            time.sleep(1)
        print(2)
        time.sleep(1)
        print('') 
        time.sleep(1)       
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 0.5:
            multiplier = 0
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


player = Fighter('Player',100,60,20)
troll = Fighter('Troll',300,30,10)

player.report()
troll.report()
print('')
time.sleep(2)

while True:
    print('player attacks the troll . . .')
    troll.defend(player.skill_attack())
    troll.report()
    time.sleep(3)
    print('')
    if troll.is_dead():
        print('you win')
        break
    print('The troll attacks you . . .')
    player.defend(troll.random_attack())
    player.report()
    time.sleep(5)
    if player.is_dead():
        print('The troll wins')
        break
    print('')