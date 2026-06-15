#Pulls random values and compiles them into interactible village.


import random, time 
store = ''

medical = ''

exotics = ''

#allows the game to create a RANDOM enemy and sends it back to the main game to take the properties
def random_vill():
    slot1 = random.randint(1, 3)
    if 1 == slot1:
        print('[the town has a merchant]') 
        time.sleep(2)
        store = 1

    elif 2 == slot1:
        print('[Theres a blacksmith in the town]')
        time.sleep(2)
        store = 2

    else:
        print('[It seems like there are no merchants in the town]')
        time.sleep(2)
        store = 3
    
    #================================================================================

    slot2 = random.randint(1, 6)
    if 3 >= slot2:
        print('[Theres a camp set up in town]') 
        time.sleep(2)
        medical = 1

    elif 5 >= slot2:
        print('[A hospital has been set up within the town]')
        time.sleep(2)
        medical = 2

    else:
        print('[The town is missing any form of hospitality]')
        time.sleep(2)
        medical = 3

    #==================================================================================

    slot3 = random.randint(1, 12)
    if 4 >= slot3:
        print('[the town has a merchant]') 
        time.sleep(2)
        exotics = 1

    elif 7 >= slot3:
        print('[Theres a blacksmith in the town]')
        time.sleep(2)
        exotics = 2

    elif 10 >= slot3:
        print('[It seems like there are no merchants in the town]')
        time.sleep(2)
        exotics = 3

    else:
        print('[The town housed nothing special]')
        exotics = 4


    #returns the value
    return store