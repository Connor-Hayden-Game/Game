#testing function implementation
import heroCreation as hc
import heroUpdate as hu
import itemCreation as ic
import random



class Hero(object):
    f = open('save.txt','r').read().splitlines()
    name                = f[0]
    health              = int(f[1])
    melee               = int(f[2])
    ranged              = int(f[3])
    magic               = int(f[4])
    points              = int(f[5])
    bank                = int(f[6])
    armor               = hu.stringToItem(f[7])
    weapon              = hu.stringToItem(f[8])
    amulet              = hu.stringToItem(f[9])
    experience          = int(f[10])
    player_level        = int(f[11])
    floor_level         = int(f[12])
    player_class        = hu.playerClass(weapon)

class Inv(object):
    f = open('inventory.txt', 'r').read().splitlines()
    item_slot1              = f[0]
    item_slot2              = f[1]
    item_slot3              = f[2]
    item_slot4              = f[3]
    item_slot5              = f[4]
    item_slot6              = f[5]
    item_slot7              = f[6]
    item_slot8              = f[7]
    item_slot9              = f[8]
    item_slot10             = f[9]
    slots                   = [item_slot1, item_slot2, item_slot3, item_slot4, item_slot5, item_slot6, item_slot7, item_slot8, item_slot9, item_slot10]


hero_obj = Hero()
hero_inv = Inv()
#hu.viewInv(hero_inv)


########################################################### Different Test Cases ########################################################################

#hu.updateInv(hero_inv, ic.random_item(hero_obj), 0, 0, hero_obj)
#hu.equipToSlot(hero_inv, hero_obj, 0)
#hu.addToInv(ic.random_item(hero_obj), hero_obj)
#hu.equipToSlot(ic.random_item(hero_obj), hero_obj)







