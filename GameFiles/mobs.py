#Making Monsters to fight

import random
import itemCreation as ic



class Monster(object):

    def __init__(self, level, mob_class, element):
        self.level         = level
        self.mob_class     = mob_class
        self.element       = element                                              
        self.health        = self.level * 2 #place holder number
        # experience         = self.level + 100
        # item_drop          = ic.random_item(level)


class Boss(object):

    def __init__(self, level, mob_class, element):
        self.level         = level
        self.mob_class     = mob_class
        self.element       = element                                              
        self.health        = self.level * 3 #place holder number
        # experience         = self.level *1.5
        # item_drop          = ic.random_item(self)
