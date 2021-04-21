#Creating a hero
import itemCreation
import heroUpdate

class Character(object):
    name                = ''
    health              = 1
    melee               = 1
    ranged              = 1
    magic               = 1
    points              = 30

    bank                = 20
    armor               = itemCreation.Item("armor", 1, "fire", "level 1 armor of fire")
    weapon              = itemCreation.Item("sword", 1, "fire", "level 1 sword of fire")
    amulet              = itemCreation.Item("amulet", 1, "fire", "level 1 amulet of fire")
    experience          = 1
    player_level        = 1
    floor_level         = 1
    player_class		= 'Brute'



    _attributes = ['name', 'health', 'melee', 'ranged', 'magic', 'points']
    def __init__(self, name):
        assert self.valid_name(name)
        self.name = name
    def add_points(self):
        accepted = ['health', 'melee', 'ranged', 'magic']
        accepted_dict = dict(enumerate(accepted, start=1))
        prompt = "\nWhich attribute?\n\t" + "\n\t".join("%d. %s"%n for n in accepted_dict.items())+"\n?"
        attribute = False
        while (attribute not in accepted):
            attribute = input(prompt)
            try:
                attribute = accepted_dict[int(attribute)]
            except:
                print ("Input was invalid. Please enter either an attribute or its corresponding number")
        amount = None
        while type(amount) != int or amount > self.points:
            try:
                amount = int(input("By how much?"))
                assert amount <= self.points
            except AssertionError:
                print ("You do not have that many points remaining")
            except:
                print ("You must enter an integer amount")
        self.__setattr__(attribute, self.__getattribute__(attribute) + amount)
        self.points -= amount
    def __str__(self):
        return "\n".join("%s\t:\t%s"%(n, self.__getattribute__(n)) for n in self._attributes)
    @staticmethod
    def valid_name(name):
        if (bool(name) and type(name) == str):
            return True
        else:
            return False
if __name__ == "__main__":
    running = True
    print ("Create a character! You have points to assign to health, melee, ranged, and magic.")
    name = ''
    while not (Character.valid_name(name)):
        name = input("Please enter your character's name:")
    CHAR = Character(name)
    OPTIONS_LIST = ["Add points", "See current attributes", "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while (running):
        CHOICE = input(PROMPT)
        try:
            CHOICE = int(CHOICE)
        except:
            pass
        if CHOICE in OPTIONS_DICT.keys():
            CHOICE = OPTIONS_DICT[CHOICE]
        if CHOICE == "Add points":
            CHAR.add_points()
        elif CHOICE == "See current attributes":
            print (CHAR)
        elif CHOICE == "Exit":
            running = False


    heroUpdate.save(CHAR)









    
