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

    item_slot1              = inventory.item_slot1
    item_slot2              = inventory.item_slot2
    item_slot3              = inventory.item_slot3
    item_slot4              = inventory.item_slot4
    item_slot5              = inventory.item_slot5
    item_slot6              = inventory.item_slot6
    item_slot7              = inventory.item_slot7
    item_slot8              = inventory.item_slot8
    item_slot9              = inventory.item_slot9
    item_slot10             = inventory.item_slot10
    slots                   = [item_slot1, item_slot2, item_slot3, item_slot4, item_slot5, item_slot6, item_slot7, item_slot8, item_slot9, item_slot10]

    inv_save = open("inventory.txt", "w")
    inv_save.write(str(inventory.slots))
    inv_save.close()


def updateInv(inventory,item, num, inv_slot, hero):

    #num is choice of adding [0]/droping [1]
    if num == 0: #adding
        inventory.slots[inv_slot] = item.name
    elif num == 1: #drop
        inventory.slots[inv_slot] = ""
    save_inv(inventory)


def equipToSlot(inventory, item, hero, inv_slot):
    if(item.item_type == "armor"):
        olditem = hero.armor
        hero.health -= int(hero.armor.item_level)
        hero.armor = item
        (hero.health) += item.item_level
        updateInv(olditem, 0, inv_slot, hero)
        
    
    elif(item.item_type == "sword" or item.item_type == "bow" or item.item_type == "staff"):
        olditem = hero.weapon
        if(olditem.item_type == "sword"):
            hero.melee -= int(hero.weapon.item_level)
        if(olditem.item_type == "bow"):
            hero.ranged -= int(hero.weapon.item_level)
        if(olditem.item_type == "staff"):
            hero.magic -= int(hero.weapon.item_level)
        hero.weapon = item
        if(item.item_type == "sword"):
            hero.melee += item.item_level
        if(item.item_type == "bow"):
            hero.ranged += item.item_level
        if(item.item_type == "staff"):
            hero.magic +=  item.item_level
        updateInv(olditem, 0, inv_slot, hero)
        
        
    elif(item.item_type == "amulet"):
        olditem = hero.amulet
        hero.health -= int(hero.amulet.item_level)
        hero.amulet = item
        (hero.health) += item.item_level
        updateInv(olditem, 0, inv_slot, hero)
    h.save(hero)
    h.save_inv(inventory)

def viewInv(inventory):
    for slot in inventory.slots:
        print(slot + '\n')

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























































