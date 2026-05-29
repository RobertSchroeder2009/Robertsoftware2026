
def battle():
    while True:
        print('player attacks the',target.name)
        target.defend(player.skill_attack())
        target.report()
        time.sleep(3)
        print('')
        if target.is_dead():
            print('you win')
            break
        print(target.name,'attacks you . . .')
        player.defend(target.random_attack())
        player.report()
        time.sleep(5)
        if player.is_dead():
            print(target.name,'wins')
            break
    print('')