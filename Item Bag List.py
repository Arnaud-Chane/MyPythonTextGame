list_item = ("dagger", "shield", "food")
health =10

hero_action = str.lower(input(""))
bag_item = "list" in hero_action
health_hero = "health" in hero_action

if bag_item == True :
	print(list(list_item))

elif health_hero == True :
	print(health)
