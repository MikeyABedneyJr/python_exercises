"""
http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:
	Keep the game going until the user types **exit**
	Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

# TODO: Add extra #2 and stop user from entering string which breaks program
import random
from random import randint
import time

secret_number = random.randint(1, 9)
print "I'm thinking of a number between 1 & 9 (including 1 & 9)."
p = 0
time.sleep(1,5)

while (p < 1):
	print ("Current secret number is: %s" % secret_number)
	user_guess = int(raw_input("Whaddya think it is?\nYour guess: "))

	if user_guess < secret_number:
		print "Toooooooo looooooooow"

	elif user_guess > secret_number:
		print "Toooooooo hiiiiiiigh"

	else:
		print "You won!"
		play_again = raw_input("If you want to quit this game, type EXIT. Otherwise press enter to play again.\n").lower()
		if (play_again == 'exit'):
			p = p + 1
		else:
			secret_number = random.randint(1, 9)
			print "A new secret number between 1 & 9 has been chosen!"
