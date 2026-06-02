import random, time 
target = ''

def generate():
    monster = random.randint(1, 3)
    if 1 == monster:
        print('[A fleshy beast approach]') 
        time.sleep(3)
        target = troll
        print('[prepare for a fight]')

    if 2 == monster:
        print('[A shadowed figure approaches, most likey a old world caster]')
        time.sleep(1)
        target = wiz
        print('[prepare for a fight]')

    if 3 == monster:
        print('[A form moves out from beyond a corner, it readys a worn bow towards you, with arrows covered in a sludge]')
        time.sleep(1)
        target = arch
        print('[prepare for a fight]')
    return target

