#hero updating
import itemCreation as ic

def save(hero):


    name        = hero.name
    health      = hero.health
    melee       = hero.melee
    ranged      = hero.ranged
    magic       = hero.magic
    points      = hero.points
    #hidden attributes

    bank		= hero.bank
    armor		= hero.armor
    weapon		= hero.weapon
    amulet		= hero.amulet
    experience	= hero.experience
    player_level= hero.player_level
    floor_level = hero.floor_level
    player_class= hero.player_class

    save = open("save.txt", "w")
    save.write(str(hero.name) + \
        "\n" + str(hero.health) + \
        "\n" + str(hero.melee)+ \
        "\n" + str(hero.ranged) + \
        "\n" + str(hero.magic)+ \
        "\n" + str(hero.points) + \
        "\n" + str(hero.bank) + \
        "\n" + str(hero.armor.name)+ \
        "\n" + str(hero.weapon.name) + \
        "\n" + str(hero.amulet.name) + \
        "\n" + str(hero.experience) + \
        "\n" + str(hero.player_level) + \
        "\n" + str(hero.floor_level) + \
        "\n" + str(hero.player_class))
    save.close()

def save_inv(inventory):

    inv_save = open("inventory.txt", "w")
    i=0
    while(i<10):
        if inventory.slots[i] == '':
            inv_save.write('\n')
        else:
            inv_save.write(inventory.slots[i] + "\n")
        i+=1
    inv_save.close()


def updateInv(inventory,item, num, inv_slot, hero):

    #num is choice of adding [0]/droping [1]
    if num == 0: #adding
        inventory.slots[inv_slot] = item.name
    elif num == 1: #drop
        inventory.slots[inv_slot] = ''
    save_inv(inventory)

def stringToItem(name_text):
    name_text = name_text.strip()  # remove all surrounding whitespace
    if not name_text:
        return None  # the text is empty

    words = name_text.split()  # split the text into word tokens

    
    level = int(words[1])
    item_type = words[2]
    item_element = words[4]
    return ic.Item(item_type, level, item_element, name_text)

def equipToSlot(inventory, hero, inv_slot):

    itemToSwap = inventory.slots[inv_slot]
    itemToSwap = stringToItem(itemToSwap)



    if(itemToSwap.item_type == "armor"):
        olditem = hero.armor
        hero.health -= int(hero.armor.item_level)
        hero.armor = itemToSwap
        (hero.health) += itemToSwap.item_level
        updateInv(inventory, olditem, 0, inv_slot, hero)
        
    
    elif(itemToSwap.item_type == "sword" or itemToSwap.item_type == "bow" or itemToSwap.item_type == "staff"):
        olditem = hero.weapon
        if(olditem.item_type == "sword"):
            hero.melee -= int(hero.weapon.item_level)
        if(olditem.item_type == "bow"):
            hero.ranged -= int(hero.weapon.item_level)
        if(olditem.item_type == "staff"):
            hero.magic -= int(hero.weapon.item_level)
        hero.weapon = itemToSwap
        if(itemToSwap.item_type == "sword"):
            hero.melee += itemToSwap.item_level
        if(itemToSwap.item_type == "bow"):
            hero.ranged += itemToSwap.item_level
        if(itemToSwap.item_type == "staff"):
            hero.magic +=  itemToSwap.item_level
        updateInv(inventory, olditem, 0, inv_slot, hero)
        hero.player_class = playerClass(itemToSwap)
        
        
    elif(itemToSwap.item_type == "amulet"):
        olditem = hero.amulet
        hero.health -= int(hero.amulet.item_level)
        hero.amulet = itemToSwap
        (hero.health) += itemToSwap.item_level
        updateInv(inventory, olditem, 0, inv_slot, hero)
    save(hero)
    save_inv(inventory)

def equipAndDrop(hero, item):

    if(item.item_type == "armor"):
        hero.health -= int(hero.armor.item_level)
        hero.armor = item
        hero.health += item.item_level

    elif(item.item_type == "sword" or item.item_type == "bow" or item.item_type == "staff"):
        if(hero.weapon.item_type == "sword"):
            hero.melee -= int(hero.weapon.item_level)        
        elif(hero.weapon.item_type == "bow"):
            hero.ranged -= int(hero.weapon.item_level)
        elif(hero.weapon.item_type == "staff"):
            hero.magic -= int(hero.weapon.item_level)
        hero.weapon = item
        if(item.item_type == "sword"):
            hero.melee += item.item_level
        if(item.item_type == "bow"):
            hero.ranged += item.item_level
        if(item.item_type == "staff"):
            hero.magic +=  item.item_level

    elif(item.item_type == "amulet"):
        hero.health -= int(hero.amulet.item_level)
        hero.amulet = item
        hero.health += item.item_level
    save(hero)

def viewInv(inventory):
    print(inventory.slots)

def playerClass(weapon):
    if(weapon.item_type == 'sword'):
        return 'Brute'
    elif(weapon.item_type == 'bow'):
        return 'Archer'
    elif(weapon.item_type == 'staff'):
        return 'Warlock'

def increaseXP(amount, hero):
    hero.experience += amount
    tmp = hero.experience
    if(hero.experience >= (10+(hero.player_level ** 2))):
        hero.experience = 0 + (tmp - (10+(hero.player_level ** 2)))
        hero.player_level += 1
        hero.points += 1
        print("You have leveled up! You are now level: ", hero.player_level)
    save(hero)



def addGold(amount, hero):
    hero.bank += amount
    save(hero)

def add_points(hero):
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
    while type(amount) != int or amount > hero.points:
        try:
            amount = int(input("By how much?"))
            assert amount <= hero.points
        except AssertionError:
            print ("You do not have that many points remaining")
        except:
            print ("You must enter an integer amount")
    hero.__setattr__(attribute, hero.__getattribute__(attribute) + amount)
    hero.points -= amount






















































