print("Oh and before i forgot :")

gender_choice = 0
while gender_choice != 1:

	print("I'm kind of blind, y'know, are you boy or a girl ?")
	print("it's not like I can rely on your voice, it's a freaking text game !")

	hero_gender = str.lower(input(""))
	boy_condition = "boy" in hero_gender
	girl_condition = "girl" in hero_gender
    gender_condition = "boy" not in hero_gender or "girl" not in hero_gender
#doesn't work very well with the not in

	if boy_condition == True :
		print("So you are a boy ?")
		break

	elif girl_condition == True :
		print("So you are a girl ?")
		break

    elif gender_condition == True :
        print("Answer the question please.")

print("In the next episode ...")