from monster_generation import generate
import random, time 
enemy = ''

#-----------------------------------------------------------

#A base class that is used for default base other class off of
class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+"'s "+ 'health: '+ str(self.__health))

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
        if multiplier < 1:
            multiplier = 0
            print('To Late!')
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

#A class using mainly 'Fighter' values but include a seperate "magic" value that is added onto the damage
class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
      super().__init__(name, starting_health, weapon, shield,)
      self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic
  
#A class that builds off the fighter class but it also allows for a new value called "Range_attack", that is randomised to be either between the original value divided by three and tripled, with the random value then added to the damage.
class Archer(Fighter):
    def __init__(self,name, starting_health, weapon, shield, Range_attack):
      super().__init__(name, starting_health, weapon, shield,)
      self.range = Range_attack

    def random_attack(self):
        attack_power = random.randint(self.weapon // 3, self.weapon*3)
        range_power = random.randint(self.range // 2, self.range*2)
        print('Ranger power:', range_power)
        print('Attack power:', attack_power)
        return attack_power + range_power
  
class Boss(Fighter):
    def __init__(self,name, starting_health, weapon, shield, ________):
      super().__init__(name, starting_health, weapon, shield,)



#The many different type values that are interchangeable 
player = Fighter('Player',110,50,20)
troll = Fighter('Fleshy form',375,30,10)
wiz = Wizard('Tainted caster',300,30,10,50)
arch = Archer('putrid archer',200,25,5,25)


#--------------------------------------------------------


target = generate()

def convert_target():
    if target == 3:
        print('arch works')
        enemy = arch
    elif target == 2:
        print('Wiz works')
        enemy = wiz
    elif target == 1:
        print('Troll works')
        enemy = troll

convert_target()
print(enemy)

target = generate()


