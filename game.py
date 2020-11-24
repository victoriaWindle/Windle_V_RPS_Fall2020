# import packages to extend python (just like we extend sublime, or atom, or VSCode)
from random import randint

#create a variable stacj - bits of data that can (and will) change

# [] => this is an array. an array is a special type of container that can hold multiple items
#arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 5
ai_lives = 5 
total_lives = 5

player = False; #True and Flase are Booleans - data types that can be truty of falsy
# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
	#print("called winorlose", status)

	if status == "won":
		pre_message = " You are the winner"
	else:
		pre_message = "you lost"

	print(pre_message + "would you like to play again?")

	print("You ", status, "! Loser. Would you like to play again?")

	choice = input ("Y / N? ")

 	if choice == "Y" or choice == "y":

 		global player_lives
 		global ai_lives
 		global player
	 	# reset the game and start over
	 	player_lives = 5
		ai_lives = 5
 		player = False

 	elif choice == "N" or choice == "n":
 		# exit message and quit
 		print("You choose to quit. Better luck next time.")
 		exit()
 	else:
		print("Make a valid choice - Y or N")
		choice = input ("Y / N? ")

while player is False: 
	# this is the player choice
	print("===================*/ RPS /*=======================")
	print("Computer lives: ", ai_lives, " / ", total_lives)
	print("Player Lives: ", player_lives, " /", total_lives)
	print("================================================")
	print("Choose your weapon! or type quit to exit.\n")
	player = input ("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	#just exit the process (kill python) and quit the game
	if player == "quit":
		print("you chose to quit, quitter!")
		exit()

	# this will be the ai choice -> a random pick from the choices array
	computer = choices[randint(0,2)]
	#check to see what the user input

	# just validate that I can make a choice
	# print outputs whatever is in the round brackets -> in this case output it to the command prompt window
	print("User chose " + player)

	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	print("user chose: " + player)

	print("AI chose " + computer)


	if (computer == player) :
		print("tie")

	elif (computer == "rock"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives) 


		else:
			print("you win!")
			ai_lives = ai_lives - 1
	elif (computer == "paper"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! Player lives: ", player_lives)

		else:
			print("you win!")
			ai_lives = ai_lives - 1

	elif (computer == "scissors") :
		if (player == "rock"):
			player_lives = player_lives - 1
			print("you lose! Player lives: ", player_lives)

		else:
			print("you win!")
			ai_lives = ai_lives - 1

	#check player lives and AI lives
elif player_lives is 0:
	winorlose("won")

	# if player_lives is 0:
	# 	print("You lost! Loser. Would you like to play again?")
	# 	choice = input ("Y / N? ")
	# 	if choice == "Y" or choice == "y":
	# 		# reset the game and start over
	# 		player_lives = 5
	# 		ai_lives = 5
	# 		player = False

	# 	elif choice == "N" or choice == "n":
	# 		# exit message and quit
	# 		print("You choose to quit. Better luck next time.")
	# 		exit()
	# 	else:
	# 		print("Make a valid choice - Y or N")

	# elif ai_lives is 0:
	# 	print("You won! Winner. Would you like to play again?")
	# 	choice = input ("Y / N? ")

	elif ai_lives is 0:
	winorlose("won")

		# if choice == "Y" or choice == "y":
		# 	# reset the game and start over
		# 	player_lives = 5
		# 	ai_lives = 5
		# 	player = False

		# elif choice == "N" or choice == "n":
		# 	# exit message and quit
		# 	print("You choose to quit. Great job!.")
		# 	exit()
		# else:
		# 	print("Make a valid choice - Y or N")

	else:
		player = False
	 #computer = choices[randint(0,2)]
