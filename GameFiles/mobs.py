#Making Monsters to fight

import random

class monster(floor_level):

	mob_list      = ["Brute", "Archer", " Warlock"]
	elements_list = ["fire", "water", "ice"]
	lvl = floor_level

    element       = random.choice(elements_list)                        #elements can be changed
    mob_type      = random.choice(mob_list)								
    health        =                                                     #fix at a later date
    experience    =  													#fix at a later date
    damage		  =  													#fix at a later date
    item_drop     = 													# random choice from drop table


class boss(floor_level):

    mob_list      = ["Brute", "Archer", " Warlock"]
    elements_list = ["fire", "water", "ice"]
	lvl = floor_level


    element       = random.choice(elements_list)                        #elements can be changed
    health        =                                                     #fix at a later date
    experience    =														#fix at a later date
    damage		  = 													#fix at a later date
    item_drop     = 													# random choice from drop table