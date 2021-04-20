#Creating Items
import random 
import heroUpdate as h



class Item(object):
	def __init__(self, item_type, item_level, item_element, name):
		self.item_type = item_type
		self.item_level = item_level
		self.item_element = item_element
		self.name = name

def random_item(hero):

	item_types = ["armor", "sword", "bow", "staff", "amulet"]
	element_list = ["fire", "water", "ice"]
	item_level = hero.floor_level
	item_type = random.choice(item_types)
	item_element =  random.choice(element_list)
	name = "level " + str(item_level) + " " + str(item_type) + " of " + str(item_element)

	return Item(item_type, item_level, item_element, name)


	

