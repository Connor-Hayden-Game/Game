#Making Monsters to fight

import random
import item_creation


class monster(floor_level, hero):

	mob_list      = ["Brute", "Archer", " Warlock"]
	elements_list = ["fire", "water", "ice"]
	lvl = floor_level

    element       = random.choice(elements_list)                        #elements can be changed
    mob_type      = random.choice(mob_list)								
    health        = floor_level * 2
    experience    = floor_level
    damage		  = floor_level
    item_drop     = random_item(hero)


class boss(floor_level, hero):

    mob_list      = ["Brute", "Archer", " Warlock"]
    elements_list = ["fire", "water", "ice"]
	lvl = floor_level


    element       = random.choice(elements_list)                        #elements can be changed
    mob_type      = random.choice(mob_list)                             
    health        = floor_level * 3
    experience    = floor_level * 2
    damage        = floor_level * 1.5
    item_drop     = random_item(hero)