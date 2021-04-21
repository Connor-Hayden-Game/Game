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
    #inventory	= hero.inventory

    save = open("save.txt", "w")
    save.write(str(hero.name) + "\n" + str(hero.health) + "\n" + str(hero.melee)+ \
    	"\n" + str(hero.ranged) + "\n" + str(hero.magic)+ "\n" + str(hero.points) + \
    	"\n" + str(hero.bank) + "\n" + str(hero.armor.item_type) + "\n" +  str(hero.armor.item_level) + "\n" +   str(hero.armor.item_element) + "\n" +  str(hero.armor.name)+ \
        "\n" + str(hero.weapon.item_type) + "\n" +  str(hero.weapon.item_level) + "\n" +   str(hero.weapon.item_element) + "\n" +  str(hero.weapon.name) + \
        "\n" + str(hero.amulet.item_type) + "\n" +  str(hero.amulet.item_level) + "\n" +   str(hero.amulet.item_element) + "\n" +  str(hero.amulet.name) + \
    	"\n" + str(hero.experience) + "\n" + str(hero.player_level) + \
        "\n" + str(hero.floor_level) + "\n" )#+ str(hero.inventory))
    save.close()

def save_inv(inventory):

    # item_slot1              = inventory.item_slot1
    # item_slot2              = inventory.item_slot2
    # item_slot3              = inventory.item_slot3
    # item_slot4              = inventory.item_slot4
    # item_slot5              = inventory.item_slot5
    # item_slot6              = inventory.item_slot6
    # item_slot7              = inventory.item_slot7
    # item_slot8              = inventory.item_slot8
    # item_slot9              = inventory.item_slot9
    # item_slot10             = inventory.item_slot10
    # slots                   = [item_slot1, item_slot2, item_slot3, item_slot4, item_slot5, item_slot6, item_slot7, item_slot8, item_slot9, item_slot10]
    print(inventory.slots[0:10])
    inv_save = open("inventory.txt", "w")
    # inv_save.write(str(slots[0]) + "\n" + str(slots[1]) + "\n" + str(slots[2]) + "\n" + str(slots[3]) + "\n" + str(slots[4]) + "\n" + str(slots[5]) + "\n"\
    #     + str(slots[6]) + "\n" + str(slots[7]) + "\n" + str(slots[8]) + "\n" + str(slots[9]))
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
    #print(inventory.slots[inv_slot])
    save_inv(inventory)

def stringToItem(name_text):
    name_text = name_text.strip()  # remove all surrounding whitespace
    if not name_text:
        return None  # the text is empty

    words = name_text.split()  # split the text into word tokens

    
    level = int(words[1])
    item_type = words[2]
    item_element = words[4]


    # if words[0] != "level":
    #     raise ValueError("Must start with 'level'")
    # try:
    #     level = int(words[1])
    # except ValueError:
    #     raise ValueError("Second word must be valid int")

    # # Now we want all of the words before "of" to be the item_type
    # # and all of the words after "of" to be the element.
    # if "of" not in words:
    #     raise ValueError("Missing 'of'")
    # item_type, element = " of ".split(" ".join(words[2:]))

    # Finally we assemble the instance and return it
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
        
        
    elif(itemToSwap.item_type == "amulet"):
        olditem = hero.amulet
        hero.health -= int(hero.amulet.item_level)
        hero.amulet = itemToSwap
        (hero.health) += itemToSwap.item_level
        updateInv(inventory, olditem, 0, inv_slot, hero)
    save(hero)
    save_inv(inventory)

def viewInv(inventory):
    print(inventory.slots)

# def equipToSlot(item, hero):
#     if(item.item_type == "armor"):
#         olditem = hero.armor
#         hero.health -= int(hero.armor.item_level)
#         hero.armor = item
#         #hero.inventory.remove(item)
#         #hero.inventory.append(olditem)
#         (hero.health) += item.item_level
#         #save(hero)
    
#     elif(item.item_type == "sword" or item.item_type == "bow" or item.item_type == "staff"):
#         olditem = hero.weapon
#         if(olditem.item_type == "sword"):
#             hero.melee -= int(hero.weapon.item_level)
#         if(olditem.item_type == "bow"):
#             hero.ranged -= int(hero.weapon.item_level)
#         if(olditem.item_type == "staff"):
#             hero.magic -= int(hero.weapon.item_level)
#         hero.weapon = item
#         #hero.inventory.remove(item)
#         #hero.inventory.append(olditem)
#         if(item.item_type == "sword"):
#             hero.melee += item.item_level
#         if(item.item_type == "bow"):
#             hero.ranged += item.item_level
#         if(item.item_type == "staff"):
#             hero.magic +=  item.item_level
#         #save(hero)
        
#     elif(item.item_type == "amulet"):
#         olditem = hero.amulet
#         hero.health -= int(hero.amulet.item_level)
#         hero.amulet = item
#         #hero.inventory.remove(item)
#         #hero.inventory.append(olditem)
#         (hero.health) += item.item_level
#     save(hero)
    


def increaseXP(amount, hero):
    hero.experience += amount
    if(hero.experience >= 10):
        hero.player_level += 1
        print("You have leveled up! You are now level: " + hero.player_level)
    save(hero)



def addGold(amount, hero):
    hero.bank += amount
    save(hero)























































