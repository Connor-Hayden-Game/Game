import itemCreation as ic
import heroUpdate as hu


def merchant(hero, inventory):
    running = True
    print ("What would you like to do?")
    OPTIONS_LIST = ["Gamble", "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while (running):
        cost = hero.floor_level * 2
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
                hu.updateInv(inventory, item, 0, 0, hero)
                hu.equipToSlot(inventory, hero, 0)
                print('You got: ' + item.name)
            else:
                print('Looks like you don\'t have enough money! Come back later.')
                running = False
        elif CHOICE == "Exit":
            running = False