#========================================================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"  

#E.G print(f"{RED}This is red text{RESET}") 
#=========================================================================

import random, time 
#makes the returned value automatically empty
target = ''

#allows the game to create a RANDOM enemy and sends it back to the main game to take the properties
def generate():
    monster = random.randint(1, 3)
    if 1 == monster:
        print(f"{RED}[A fleshy beast approaches]{RESET}") 
        time.sleep(2)
        target = 1
        print('[prepare for a fight]')

    if 2 == monster:
        print(f"{RED}[A shadowed figure approaches, most likey a old world caster]{RESET}")
        time.sleep(3)
        target = 2
        print('[prepare for a fight]')

    if 3 == monster:
        print(f"{RED}[A form moves out from beyond a corner, it readys a worn bow towards you, with arrows covered in a sludge]{RESET}")
        time.sleep(4)
        target = 3
        print('[prepare for a fight]')
        time.sleep(2)
    
    #returns the value
    return target