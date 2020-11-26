# import packages to extend python (just like we extend sublime, or atom, or VSCode)
from random import randint

#re-import our game variables
from GameComponents import gameVars, winLose

while gameVars.player is False: 
	# this is the player choice
	print("===================*/ RPS /*=======================")
	print("Computer lives: ", gameVars.ai_lives, " / ", gameVars.total_lives)
	print("Player Lives: ", gameVars.player_lives, " /", gameVars.total_lives)
	print("================================================")
	print("Choose your weapon! or type quit to exit.\n")
	gameVars.player = input ("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	#just exit the process (kill python) and quit the game
	if gameVars.player == "quit":
		print("you chose to quit, quitter!")
		exit()

	# this will be the ai choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0,2)]
	#check to see what the user input

	# just validate that I can make a choice
	# print outputs whatever is in the round brackets -> in this case output it to the command prompt window
	print("User chose: " + gameVars.player)

	#validate that the random choice worked for the AI
	print("AI chose: " + computer)

	#print("user chose: " + gameVars.player)

	#print("AI chose: " + computer)


	if (computer == gameVars.player) :
		print("tie")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives = gameVars.player_lives - 1
			print("you lose! player lives: ", gameVars.player_lives) 


		else:
			print("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1
	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives = gameVars.player_lives - 1
			print("you lose! Player lives: ", gameVars.player_lives)

		else:
			print("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1

	elif (computer == "scissors") :
		if (gameVars.player == "rock"):
			gameVars.player_lives = gameVars.player_lives - 1
			print("you lose! Player lives: ", gameVars.player_lives)

		else:
			print("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1

	#check player lives and AI lives
	if gameVars.player_lives is 0:
		winLose.winorlose("lost")

	elif gameVars.ai_lives is 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

