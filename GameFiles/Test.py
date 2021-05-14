#testing function implementation
import heroCreation as hc
import heroUpdate as hu
import itemCreation as ic
import random
from mobs import Monster
import combat

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



mob_list           = ["Brute", "Archer", " Warlock"]
elements_list      = ["fire", "water", "earth"]



hero_obj = Hero()
hero_inv = Inv()
#mob = Monster(hero_obj.floor_level, random.choice(mob_list), random.choice(elements_list))
mob = Monster(hero_obj.floor_level, random.choice(mob_list), random.choice(elements_list))
#hu.viewInv(hero_inv)
item = ic.random_item(hero_obj)




########################################################### Different Test Cases ########################################################################


############# Testing eternal
# counter=0
# while(True):
#     if(item.item_element != 'eternal'):
#         item = ic.random_item(hero_obj)
#         counter +=1
#         print(counter)
#     else:
#         print(item.name)
#         break


############# First combat Test
# print(mob.health)
# print(mob.element)
# print(mob.mob_class)
# print(combat.damageDone(hero_obj, mob)) 

############# Second combat Test
# print(mob.health)
# print(mob.element)
# print(mob.mob_class)
# print(combat.damageReceived(hero_obj, mob)) 

############# Combat Sequence Test
combat.combatSequence(hero_obj, mob)


############ Inv updates
#hu.updateInv(hero_inv, ic.random_item(hero_obj), 0, 0, hero_obj)
#hu.equipToSlot(hero_inv, hero_obj, 0)
#hu.addToInv(ic.random_item(hero_obj), hero_obj)
#hu.equipToSlot(ic.random_item(hero_obj), hero_obj)

########### EXP Tests
# hu.increaseXP(220, hero_obj)






