import random, time 

def shop_randomising():

    #prints the first random value for the store
    slot1 = random.randint(1, 5)
    if 1 == slot1:
        storeA = 1

    elif 2 == slot1:
        storeA = 2
        
    elif 3 == slot1:
        storeA = 3
        
    elif 4 == slot1:
        storeA = 4
        
    elif 5 == slot1:
        storeA = 5

    else:
        print('error')


    #prints the second random value for the store
    slot2 = random.randint(1, 5)
    if 1 == slot2:
        storeB = 1

    elif 2 == slot2:
        storeB = 2
        
    elif 3 == slot2:
        storeB = 3
        
    elif 4 == slot2:
        storeB = 4
        
    elif 5 == slot2:
        storeB = 5
    else:
        print('error')

    #prints the third random value for the store
    slot2 = random.randint(1, 5)
    if 1 == slot2:
        storeB = 1

    elif 2 == slot2:
        storeB = 2
        
    elif 3 == slot2:
        storeB = 3
        
    elif 4 == slot2:
        storeB = 4
        
    elif 5 == slot2:
        storeB = 5
    else:
        print('error')

        #prints the fourth random value for the store
    slot2 = random.randint(1, 5)
    if 1 == slot2:
        storeB = 1

    elif 2 == slot2:
        storeB = 2
        
    elif 3 == slot2:
        storeB = 3
        
    elif 4 == slot2:
        storeB = 4
        
    elif 5 == slot2:
        storeB = 5
    else:
        print('error')
    
        #prints the fifth random value for the store
    slot2 = random.randint(1, 5)
    if 1 == slot2:
        storeB = 1

    elif 2 == slot2:
        storeB = 2
        
    elif 3 == slot2:
        storeB = 3
        
    elif 4 == slot2:
        storeB = 4
        
    elif 5 == slot2:
        storeB = 5
    else:
        print('error')
    
    return storeA, storeB, storeC, storeD, storeE



storeA = shop_randomising()

print(storeA)