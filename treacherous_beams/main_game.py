#Allows for the use of random clauses
import random, time 
from story_code import story
from monster_generation import generate
from yes_no_def import yes_no
import sys


#-----------------------------------
#allowing text to be coloured

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"  

#E.G "  print(f"{RED}This is red text{RESET}")  "
#-----------------------------------

#Calls upon the other file to print the story
#[<---REMOVE HASH TO PLAY STORY]  story()

time.sleep(2)

#A base class that is used for default base other class off of
class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(f"{GREEN}{self.name}'s health: {str(self.__health)}{RESET}")
        

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
        enemy = random.randint(2,6)
        print('Hit enter when you see the X')
        time.sleep(1)
        print(f"{GREEN}Ready...{RESET}")
        time.sleep(1)
        tic = time.time()

        if enemy == 6:
            print(f'{RED}___{RESET}')
            time.sleep(1)

        if enemy >= 5:
            print(f'{RED}___{RESET}')
            time.sleep(1)

        if enemy >= 4:
            print(f'{RED}___{RESET}')
            time.sleep(1)

        if enemy >= 3:
            print(f'{RED}___{RESET}')
            time.sleep(1)

        print(f'{RED}___{RESET}')
        time.sleep(1)

        print(f'{RED}___{RESET}') 
        time.sleep(1)  

        print(f'{GREEN}_X_{RESET}')     
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(enemy-time_taken)
        if multiplier < 1:
            multiplier = 0
            print(f'{RED}To Late!{RESET}')
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print(f'{RED}Damage: {damage}{RESET}')
        else:
            print(f'{GREEN}No damage{RESET}')

#A class using mainly 'Fighter' values but include a seperate "magic" value that is added onto the damage
class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic):
      super().__init__(name, starting_health, weapon, shield,)
      self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic
    
    def restore_health(self,starting_health):
        self.__health = starting_health

#A class that builds off the fighter class but it also allows for a new value called "Range_attack", that is randomised to be either between the original value divided by three and tripled, with the random value then added to the damage.
class Archer(Fighter):
    def __init__(self,name, starting_health, weapon, shield, Range_attack):
      super().__init__(name, starting_health, weapon, shield,)
      self.range = Range_attack

    def random_attack(self):
        attack_power = random.randint(self.weapon // 3, self.weapon*3)
        range_power = random.randint(self.range // 5, self.range*5)
        print('Ranger power:', range_power)
        print('Attack power:', attack_power)
        return attack_power + range_power
    
    def restore_health(self,starting_health):
        self.__health = starting_health
   
#Turns the value from the other file into a enemy to fight
def approach():
    target = generate()
    if target == 3:
        enemy = arch

    elif target == 2:
        enemy = wiz

    elif target == 1:
        enemy = troll
    return enemy
    
#Contains all the values and comands for the fights
def battle():
    while True:
        print('')
        print('------------------------------------------------------')
        print(f'{GREEN}player attacks the {enemy.name}{RESET}')
        enemy.defend(player.skill_attack())
        enemy.report()
        time.sleep(3)
        print('')
        if enemy.is_dead():
            print(f'{GREEN}you win{RESET}')
            break
        print(f'{RED}{enemy.name} attacks you . . .{RESET}')
        player.defend(enemy.random_attack())
        player.report()
        time.sleep(3)
        if player.is_dead():
            print(f"{RED}{enemy.name} wins{RESET}")
            time.sleep(2)
            break
        print('')


#--------------------------------------

#The many different type values that are interchangeable 
player = Fighter('Player',110,50,25)
troll = Fighter('Fleshy form',300,30,10)
wiz = Wizard('Tainted caster',225,30,10,50)
arch = Archer('putrid archer',180,20,5,25)

#takes the value and turns it into a enermy to fight
enemy = approach()


player.report()
enemy.report()
print('')
time.sleep(2)

battle()

#checks if the player alive or dead
if enemy.is_dead():
    print(f'{GREEN}Player survived{RESET}')
else:
    print(f'{RED}GAME OVER{RESET}')
    sys.exit(0)
#---------------------------------------

#Checks and prompts the player whether they want to fight another enemy or just finish the game
print('')
print('Would you like to play again?')
time.sleep(1)
yesno = yes_no()


if yes_no == True:
    enemy = approach()
    
    #Heals the enemy
    enemy.restore_health()
    
    player.report()
    enemy.report()
    print('')
    time.sleep(2)

    #starts the battle again with the player at the same health they won the battle at
    battle()
else:
    #ends the game
    sys.exit(0)