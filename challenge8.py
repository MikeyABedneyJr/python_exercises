"""
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
import random

p = 1

while (p < 2):
	user_move = raw_input("Rock, Paper Scissors is fun for the whole family! Please choose one of the following options: \nRock\nPaper\nScissors\n:").lower()

	move_options = ['rock', 'paper', 'scissors']

	computer_move = random.choice(move_options)


	print ("Human chooses %s and computer chooses %s" % (user_move,computer_move))

	if (user_move == 'rock' and computer_move == 'scissors'):
		print "The human wins!"

	elif (user_move == 'paper' and computer_move == 'rock'):
		print "The human wins!"

	elif (user_move == 'scissors' and computer_move == 'paper'):
		print "The human wins!"

	elif (user_move == computer_move):
		print "It's a tie!"

	else:
		print "The computer wins!"

	play_again = raw_input("Did you want to play again? Answer 'yes' or 'no': ").lower()

	if (play_again == 'no'):
		p = p + 1
