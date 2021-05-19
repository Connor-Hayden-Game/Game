import itemCreation as ic
import heroUpdate as hu
import random

def merchant(hero):
    running = True
    print ("What would you like to do?")
    OPTIONS_LIST = ["Gamble", "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while (running):
        cost = hero.player_level * 2
        print('It costs: ', cost, 'to Gamble.')
        CHOICE = input(PROMPT)
        try:
            CHOICE = int(CHOICE)
        except:
            pass
        if CHOICE in OPTIONS_DICT.keys():
            CHOICE = OPTIONS_DICT[CHOICE]
        if CHOICE == "Gamble":
            if(hero.bank > cost):
                hero.bank -= cost
                item = ic.random_item(hero)
                print('You got: ' + item.name)
                op = input("Would you like to keep and equip it? [y/n]")
                if(op.lower() == ("y" or "yes")):
                    hu.equipAndDrop(hero, item)
                else:
                    pass
                hu.save(hero)
            else:
                print('Looks like you don\'t have enough money! Come back later.')
                running = False
        elif CHOICE == "Exit":
            running = False


def coinFlip(hero):
    running =True
    OPTIONS_LIST = ["Heads", "Tails"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while (running):
        cost = int(input('How much would you like to bet?'))
        if(cost <= hero.bank):
            hero.bank -= cost
            CHOICE = input(PROMPT)
            if(CHOICE == '1'):
                guess = "Heads"
            elif(CHOICE == '2'):
                guess = "Tails"
            else:
                print("Invalid guess")
                break
            winner = random.choice(OPTIONS_LIST)
            print(winner)
            if guess == winner:
                hero.bank += cost * 2
                print("You've won ", cost, "!")
                print("You know have " + str(hero.bank) + " gold.")
            else:
                print("You lost, better luck next time.")
            hu.save(hero)
            running = False
        else:
            print("You don't have that much money!")
            running = False


























