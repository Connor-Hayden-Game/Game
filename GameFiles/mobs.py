#Making Monsters to fight

import random
import itemCreation as ic



class Monster(object):

    def __init__(self, level, mob_class, element):
        self.level         = level
        self.mob_class     = mob_class
        self.element       = element                                              
        self.health        = self.level * 2
        experience         = self.level
        item_drop          = ic.random_item(self)


class boss(object):

    def __init__(self, level, mob_class, element):
        self.level         = level
        self.mob_class     = mob_class
        self.element       = element                                              
        self.health        = self.level * 3
        experience         = self.level *1.5
        item_drop          = ic.random_item(self)