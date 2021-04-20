#hero updating



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


def load(hero):
    f = open("save.txt", "r")
    hero.name                = f.readline()
    hero.health              = f.readline()
    hero.melee               = f.readline()
    hero.ranged              = f.readline()
    hero.magic               = f.readline()
    hero.points              = f.readline()
    hero.bank                = f.readline()
    hero.armor               = f.readline()
    hero.weapon              = f.readline()
    hero.amulet              = f.readline()
    hero.experience          = f.readline()
    hero.player_level        = f.readline()
    hero.floor_level         = f.readline()
    '''hero.inventory           = f.readline()'''
    f.close()

'''
def addToInv(item, hero):
    hero.inventory.append(item)
    save(hero)
'''
def equipToSlot(item, hero):
    if(item.item_type == "armor"):
        olditem = hero.armor
        hero.health -= int(hero.armor.item_level)
        hero.armor = item
        #hero.inventory.remove(item)
        #hero.inventory.append(olditem)
        (hero.health) += item.item_level
        #save(hero)
    
    elif(item.item_type == "sword" or item.item_type == "bow" or item.item_type == "staff"):
        olditem = hero.weapon
        if(olditem.item_type == "sword"):
            hero.melee -= int(hero.weapon.item_level)
        if(olditem.item_type == "bow"):
            hero.ranged -= int(hero.weapon.item_level)
        if(olditem.item_type == "staff"):
            hero.magic -= int(hero.weapon.item_level)
        hero.weapon = item
        #hero.inventory.remove(item)
        #hero.inventory.append(olditem)
        if(item.item_type == "sword"):
            hero.melee += item.item_level
        if(item.item_type == "bow"):
            hero.ranged += item.item_level
        if(item.item_type == "staff"):
            hero.magic +=  item.item_level
        #save(hero)
        
    elif(item.item_type == "amulet"):
        olditem = hero.amulet
        hero.health -= int(hero.amulet.item_level)
        hero.amulet = item
        #hero.inventory.remove(item)
        #hero.inventory.append(olditem)
        (hero.health) += item.item_level
    save(hero)
    


def increaseXP(amount, hero):
    hero.experience += amount
    if(hero.experience >= 10):
        hero.player_level += 1
        print("You have leveled up! You are now level: " + hero.player_level)
    save(hero)



def addGold(amount, hero):
    hero.bank += amount
    save(hero)























































