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

# Generate secret number, set a counter, explain the game, and pause. p=0 is used to exit 
# the while loop gracefully rather than throwing an error.
secret_number = random.randint(1, 9)
print "I'm thinking of a number between 1 & 9 (including 1 & 9)."
p = 0
time.sleep(1.5)
counter = 0

while (p < 1):

	# The print statement below is for testing purposes
	# print ("Current secret number is: %s" % secret_number)
	
	user_guess = int(raw_input("Whaddya think it is?\nYour guess: "))
	
	# The print statement below helped to see if the counter was working correctly
	# print "You are currently on guess number: %s" % counter

	time.sleep(1.5)
	
	# Now they are on their first guess. If they get it wrong, this will add another
	# +1 to the counter to keep track of their guesses
	counter += 1

	# Evaluate the number that is guessed & give feedback
	if user_guess < secret_number:
		print "Toooooooo looooooooow"
		
	elif user_guess > secret_number:
		print "Toooooooo hiiiiiiigh"


	else:
		print ("You won! Number of guesses: %s" % counter)
		time.sleep(1.5)

		# Ask user if they want to play again
		play_again = raw_input("If you want to quit this game, type EXIT. Otherwise press enter to play again.\n").lower()

		# Stop the game on 'exit'
		if (play_again == 'exit'):
			p = p + 1
			print "Oh I get it...we're done here then. It's fine. I'll be fine...just go...."
		
		# User chooses to play again, make a new number and reset the counter. While loop
		# continues...
		else:
			secret_number = random.randint(1, 9)
			counter = 0
			print "A new secret number between 1 & 9 has been chosen!"
