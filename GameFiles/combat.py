import mobs
import heroUpdate as hu



def damageDone(hero, monster):
	playerDamageType 					= ''
	playerElementType 					= ''
	mobDamageType 						= monster.mob_class
	mobElementType 						= monster.mob_class
	typeMultiplier 						= 0
	elementMultiplier 					= 0
	dmg 								= 0

	if(hero.player_class == 'Brute'):
		playerDamageType = "melee"
	elif(hero.player_class == 'Archer'):
		playerDamageType = "ranged"		
	elif(hero.player_class == 'Warlock'):
		playerDamageType = "magic"

	if(hero.weapon.item_element == "fire"):
		playerElementType = 'fire'
	elif(hero.weapon.item_element == "water"):
		playerElementType = 'water'
	elif(hero.weapon.item_element == "earth"):
		playerElementType = 'earth'

	if(playerDamageType == 'melee'):
		if(mobDamageType == 'Brute'):
			typeMultiplier = 0.0
		if(mobDamageType == 'Archer'):
			typeMultiplier = 0.2
		if(mobDamageType == 'Warlock'):
			typeMultiplier = -0.2
	elif(playerDamageType == 'ranged'):
		if(mobDamageType == 'Brute'):
			typeMultiplier = -0.2
		if(mobDamageType == 'Archer'):
			typeMultiplier = 0.0
		if(mobDamageType == 'Warlock'):
			typeMultiplier = 0.2
	elif(playerDamageType == 'magic'):
		if(mobDamageType == 'Brute'):
			typeMultiplier = 0.2
		if(mobDamageType == 'Archer'):
			typeMultiplier = -0.2
		if(mobDamageType == 'Warlock'):
			typeMultiplier = 0.0

	if(playerElementType == 'fire'):
		if(mobElementType == 'fire'):
			elementMultiplier = 0.0
		if(mobElementType == 'water'):
			elementMultiplier = -0.3
		if(mobElementType == 'earth'):
			elementMultiplier = 0.3
	elif(playerElementType == 'water'):
		if(mobElementType == 'fire'):
			elementMultiplier = 0.3
		if(mobElementType == 'water'):
			elementMultiplier = 0.0
		if(mobElementType == 'earth'):
			elementMultiplier = -0.3
	elif(playerElementType == 'earth'):
		if(mobElementType == 'fire'):
			elementMultiplier = -0.3
		if(mobElementType == 'water'):
			elementMultiplier = 0.3
		if(mobElementType == 'earth'):
			elementMultiplier = 0.0

	damage_multiplier = 1 + elementMultiplier + typeMultiplier

	if(hero.player_class == 'Brute'):
		dmg = hero.melee  * damage_multiplier
	elif(hero.player_class == 'Archer'):
		dmg = hero.ranged  * damage_multiplier	
	elif(hero.player_class == 'Warlock'):
		dmg = hero.magic  * damage_multiplier

	return dmg



# def damageRecieved(hero, mob):
