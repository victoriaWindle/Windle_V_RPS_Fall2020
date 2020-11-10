# import packages to extend python (just like we extend sublime, or atom, or VSCode)
from random import randint

# [] => this is an array. an array is a special type of container that can hold multiple items
#arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

# this is the player choice
player = input ("Choose rock, paper or scissors: ")

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

if (computer == player)
	print("tie")

elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!")

	else:
		print("you win!")

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose!")

	else:
		print("you win!")

	elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose!")

	else:
		print("you win!")