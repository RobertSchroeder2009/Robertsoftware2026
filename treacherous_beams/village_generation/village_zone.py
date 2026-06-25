#Pulls random values and compiles them into interactible village.

#========================================================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
RESET = "\033[0m"  

#E.G "  print(f"{RED}This is red text{RESET}")  "

#=========================================================================

import random, time 

#This pulls and compiles a long randomisation of the places that the village has
def random_vill():
    print('=============================================================')
    print('')
    slot1 = random.randint(1, 3)
    if 1 == slot1:
        print(f"{GREEN}[the town has a merchant]{RESET}")
        print(' --type 1 to check the merchants wares-- ')
        time.sleep(2)
        store = 1

    elif 2 == slot1:
        print(f"{BLUE}[Theres a blacksmith in the town]{RESET}")
        print('  --type 1 to check the blacksmiths wares-- ')
        time.sleep(2)
        store = 2

    else:
        print(f"{RED}[It seems like there are no merchants in the town]{RESET}")
        time.sleep(2)
        store = 3
    print('')
    #================================================================================

    slot2 = random.randint(1, 6)
    if 3 >= slot2:
        print(f"[{GREEN}Theres a camp set up in town]{RESET}") 
        print(" --type 2 to rest-- [recover 50 health points]")
        time.sleep(2)
        medical = 1

    elif 5 >= slot2:
        print(F"{BLUE}[A hospital has been set up within the town]{RESET}")
        print(' --type 2 to vistit the hospital-- [recovers all health points]')
        time.sleep(2)
        medical = 2

    else:
        print(f"{RED}[The town is missing any form of hospitality]{RESET}")
        time.sleep(2)
        medical = 3
    print('')

    #==================================================================================

    slot3 = random.randint(1, 18)
    if 6 >= slot3:
        print(f"{GREEN}[A well has been dug out in the centre of the village]{RESET}")
        print(' --type 3 to draw water from the well-- ')
        time.sleep(2)
        exotics = 1

    elif 9 >= slot3:
        print(f"{BLUE}[A training area has been set up in the middle of the town]{RESET}")
        print(' --type 3 to increase your strength at the arena-- ')
        time.sleep(2)
        exotics = 2

    elif 11 >= slot3:
        print(F"{BLUE}[A trader has set up within the town, it seems like the have some {YELLOW}exotic goods]{RESET}")
        print(' --type 3 to view the exotics traders goods-- ')
        time.sleep(2)
        exotics = 3
    
    elif 12 == slot3:
        print(f"{YELLOW}[Theres a weird {RED}hole in the Earth... {YELLOW}maybe a bunker... {RED}or maybe a hole to hell...]{RESET}")
        print(' --type 3 to descend the hole-- ')
        exotics = 4

    else:
        print(f"{RED}[The town housed nothing special]{RESET}")
        exotics = 5
    print('')
    print('=============================================================')


    #returns the value
    return store, medical, exotics