#testing function implementation
import heroCreation as hc
import heroUpdate as hu
import itemCreation as ic
import random
from mobs import Monster
from mobs import Boss
import combat
import merchant as me

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
    experience          = float(f[10])
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
elements_list      = ["fire" *100, "water" * 100, "earth" * 100, "eternal"]



hero_obj = Hero()
hero_inv = Inv()
#mob = Monster(hero_obj.floor_level, random.choice(mob_list), random.choice(elements_list))
#mob = Monster(hero_obj.floor_level, random.choice(mob_list), random.choice(elements_list))
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
#combat.combatSequence(hero_obj, mob)


############ Inv updates
#hu.updateInv(hero_inv, ic.random_item(hero_obj), 0, 0, hero_obj)
#hu.equipToSlot(hero_inv, hero_obj, 0)
#hu.addToInv(ic.random_item(hero_obj), hero_obj)
#hu.equipToSlot(ic.random_item(hero_obj), hero_obj)

########### EXP Tests
# hu.increaseXP(220, hero_obj)


########## Full game Test

def main():

    running = True
    print ("What would you like to do?")
    OPTIONS_LIST = ["See Hero Attributes", "Add Points", "Change floor level", "Fight Mobs", "Merchant", "Coin Flip",  "Exit"]
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
        if CHOICE == "See Hero Attributes":
            print( \
                "Name    : " + str(hero_obj.name)                                                              + "\n" \
                "Health  : " + str(hero_obj.health)                                                            + "\n" \
                "Melee   : " + str(hero_obj.melee)                                                             + "\n" \
                "Ranged  : " + str(hero_obj.ranged)                                                            + "\n" \
                "Magic   : " + str(hero_obj.magic)                                                             + "\n" \
                "Points  : " + str(hero_obj.points)                                                            + "\n" \
                "Money   : " + str(hero_obj.bank)                                                              + "\n" \
                "Exp     : " + str(hero_obj.experience)   + "/" + str(float(10+(hero_obj.player_level ** 2))) + "\n" \
                "Level   : " + str(hero_obj.player_level)                                                      + "\n" \
                "Floor   : " + str(hero_obj.floor_level)                                                       + "\n" \
                "Weapon  : " + str(hero_obj.weapon.name)                                                       + "\n" \
                "Armor   : " + str(hero_obj.armor.name)                                                        + "\n" \
                "Amulet  : " + str(hero_obj.amulet.name)                                                       + "\n" 
             )
        elif CHOICE == "Add Points":
            hu.add_points(hero_obj)
        elif CHOICE == "Change floor level":
            tmp_level = input("What level would you like? \n")
            hero_obj.floor_level = int(tmp_level)
        elif CHOICE == "Fight Mobs":
            mob = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            combat.combatSequence(hero_obj, mob)
            mob2 = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            combat.combatSequence(hero_obj, mob2)
            mob3 = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            combat.combatSequence(hero_obj, mob3)
            print("Get ready for the Boss!")
            mob4= Boss((int(hero_obj.floor_level) +1), random.choice(mob_list), random.choice(elements_list))
            combat.combatSequence(hero_obj, mob4)

        elif CHOICE == "Merchant":
            me.merchant(hero_obj)
        elif CHOICE == "Coin Flip":
            me.coinFlip(hero_obj)
        elif CHOICE == "Exit":
            running = False

main()





