import random, time 
Sty = ""
yynn = ["Yes", "yes", "No", "no"]



def story():
    print('Once upon a time, people looked at the sun in hope and warmth...')
    time.sleep(5)
    print('then, once upon a time, it burned the eyes of all those pitiful fools that looked upon it with hope and warmth...')
    time.sleep(9)
    print('now the sands that encase the earth are filled with the ash of all the souls that once lived...')
    time.sleep(7)
    print('')
    print('except for a few...')
    time.sleep(3)
    print('a tiny amount of people...')
    time.sleep(4)
    print('and after generations bloody hands and smoked flesh...')
    time.sleep(4)
    print('roots could finally sprout...')
    time.sleep(4)
    print('and the little life that spread the Earth...')
    time.sleep(4)
    print('started adapting...')
    time.sleep(4)
    print('villages rised and sands shifted...')
    time.sleep(3)
    print('')
    print('but the scars are stil lying in wait...')
    time.sleep(4)
    print('still hunger...')
    time.sleep(2)
    print('still hunt...')
    time.sleep(3)
    print('and those generations of fight and will...')
    time.sleep(4)
    print('fuel the hives of rotten and bloated flesh...')
    time.sleep(6)
    print('proof that not even the heat of hell can wipe the hate and filth off the flesh of man.')
    time.sleep(7)
    print('')

    print('')
    print('but now you stand...')
    time.sleep(3)
    print('alone...')
    time.sleep(3)
    print('in a land of not what you know of...')
    time.sleep(4)

 #-----------------------------------

    print('---------------------')
    print('')
    print("Do you know your backstory[Yes/No]")
    Sty = input("")
    print('')

    while Sty not in yynn:
       print("Please type it with a capital letter")
       Sty = input('')

    if 'Yes' in Sty:
        Story = input('[Please type you backstory here] ')
        print('')
        print('Oh wow such a interesting story...')
        print(f'Really? {Story}?')

    elif 'yes' in Sty:
        Story = input('[Please type you backstory here]')
        print('')
        print('Oh wow such a interesting story...')
        print(f'Really? {Story}?')


    elif 'No' in Sty:
        print('A story will be randomly selected for you')

    elif 'no' in Sty:
        print('A story will be randomly selected for you')