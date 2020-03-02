#First Text-Game in Python, So exited !!!
#Long journey in coming ;)
#Enjoy it <3

print("Hello Stranger ! What's your name ?")
name = input("??? - My name is ")
print(f"Oh, hello {name}.")


#while loop pr revenir à la question initiale
choice = 0
while choice != 1 :

	print("So now, where do you want to go ? Left or Right ? ")


	DirectionHero = input("I think I'll go ")
	DirectionHero = str.lower(DirectionHero)

	if DirectionHero == "left":
    		print("Good choice. The  adventure begins here ...")
    		break
    
	elif DirectionHero == "right":
    		print(f"Nope, right to hell you go {name} ! Just kidding, just follow me.")
    		break
    		

	else :
		   	print("Sorry, I didn't catch that ...")
		   	
		   	
		   	
print("So, let's choose a class :")

class_choice = 0
while class_choice != 1 :

	print("You can be either a warrior or a mage, which one do you wanna be ?")

	hero_class = input("I'm gonna be a ")
	hero_class = str.lower(hero_class)


	if hero_class == "warrior":
		attack = 30
		magic = 5
		health = 100
		regen = 10
		print("Good ! Then, you are a warrior my friend !")
		break

	elif hero_class == "mage":
		attack = 5
		magic = 50
		health = 100
		regen = 5
		print("Yeah ! Mage rocks ! *huh huh* Ok, let's go ...")
		break

	else :
		print("Say whaaaaaaaaaat ?")
		print("No seriously, answer. Which one ?")


print("Oh and before i forgot :")

gender_choice = 0
while gender_choice != 1:

	print("I'm kind of blind, y'know, are you boy or a girl ?")
	print("it's not like I can rely on your voice, it's a freaking text game !")

	hero_gender = str.lower(input(""))
	boy_condition = "boy" in hero_gender
	girl_condition = "girl" in hero_gender

	if boy_condition == True :
		print("So you are a boy ?")
		break

	elif girl_condition == True :
		print("So you are a girl ?")
		break


print("In the next episode ...")