from random import randint
from GameComponents import gameVars


def compare(status):

	#validate that the random choice worked for the AI
		#print("AI chose: " + comparison.computer)
	computer = gameVars.choices[randint(0,2)]
	print("AI chose: " + computer)

	if (computer == gameVars.player) :
			print ("tie")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives = gameVars.player_lives - 1
			print ("you lose! player lives: ", gameVars.player_lives) 

		else:
			print ("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			gameVars.player_lives = gameVars.player_lives - 1
			print ("you lose! Player lives: ", gameVars.player_lives)

		else:
			print ("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1

	elif (computer == "paper") :
		if (gameVars.player == "rock"):
			gameVars.player_lives = gameVars.player_lives - 1
			print ("you lose! Player lives: ", gameVars.player_lives)

		else:
			print ("you win!")
			gameVars.ai_lives = gameVars.ai_lives - 1
		