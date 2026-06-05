import random, time 
Sty = ""
yynn = ["Yes", "yes", "No", "no"]
yesno = False

#--------------------------------
#Allows for colours
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

#resets the colour
RESET = "\033[0m"  

#---------------------------------
#creates prompt the player to enter yes or no, it also can take both yes/no with capital letters or just uncapped letter
def yes_no():
    print(f"[Yes/No]")
    Sty = input("")
    print('')

    while Sty not in yynn:
       print("Please type only a yes or no")

    yesno = False

    if 'Yes' in Sty:
        yesno = True

    elif 'yes' in Sty:
        yesno = True


    elif 'No' in Sty:
        yesno = False

    elif 'no' in Sty:
        yesno = False

 #returns the players response
    return yesno
