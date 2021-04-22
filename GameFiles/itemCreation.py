#Creating Items
import random 
#import heroUpdate as h
# import heroCreation



class Item(object):
    def __init__(self, item_type, item_level, item_element, name):
        self.item_type = item_type
        self.item_level = item_level
        self.item_element = item_element
        self.name = name

def random_item(hero):

    item_types = ["armor", "sword", "bow", "staff", "amulet"]
    element_list = ["fire", "water", "earth"]
    item_level = hero.floor_level
    item_type = random.choice(item_types)
    item_element =  random.choice(element_list)
    name = "level " + str(item_level) + " " + str(item_type) + " of " + str(item_element)

    return Item(item_type, item_level, item_element, name)


    

class Inventory(object):
    
    item_slot1              = ''
    item_slot2              = ''
    item_slot3              = ''
    item_slot4              = ''
    item_slot5              = ''
    item_slot6              = ''
    item_slot7              = ''
    item_slot8              = ''
    item_slot9              = ''
    item_slot10             = ''
    slots                   = [item_slot1, item_slot2, item_slot3, item_slot4, item_slot5, item_slot6, item_slot7, item_slot8, item_slot9, item_slot10]


