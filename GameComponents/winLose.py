from GameComponents import gameVars

def winorlose(status):
	#print("called winorlose", status)

	if status == "won":
		pre_message = " You are the winner!"
	else:
		pre_message = "You lost!"

	print(pre_message + "would you like to play again?")

	print("You ", status, "! Loser. Would you like to play again?")

	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":

		# reset the game and start over
		gameVars.player_lives = 5
		gameVars.ai_lives = 5
		gameVars.player = False

	elif choice == "N" or choice == "n":
 		# exit message and quit
 		print("You choose to quit. Better luck next time.")
 		exit()
	else:
		print("Make a valid choice - Y or N")
		choice = input ("Y / N? ")