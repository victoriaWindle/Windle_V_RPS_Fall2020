# import packages to extend python (just like we extend sublime, or atom, or VSCode)
#from random import randint

#re-import our game variables
from GameComponents import gameVars, winLose, comparison

while gameVars.player is False: 
	# this is the player choice
	print("===================*/ RPS /*=======================")
	print("Computer lives: ", gameVars.ai_lives, " / ", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, " /", gameVars.total_lives)
	print("================================================")

	while gameVars.player != 0 or gameVars.ai_lives !=0:
		print("Choose your weapon! or type quit to exit.\n")

		gameVars.player = input ("Choose rock, paper or scissors: \n")



	# if the player chooses to quit, then don't do anything else
	#just exit the process (kill python) and quit the game
		if gameVars.player == "quit":
			print("you chose to quit, quitter!")
			exit()

	# print outputs whatever is in the round brackets -> in this case output it to the command prompt window
		print("User chose: " + gameVars.player)

		# != is does not equal
	#while gameVars.player != 0 or gameVars.ai_lives !=0:
		
		comparison.compare(gameVars.player)
		
		#check player lives and AI lives
		if gameVars.player_lives is 0:
				winLose.winorlose("lost")

		elif gameVars.ai_lives is 0:
				winLose.winorlose("won")

		else:
			gameVars.player = False

