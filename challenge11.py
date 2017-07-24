# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not. 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions.

# Get an integer from the user. If it's not a number, prompt them again.
def get_number(user_number="Please give me a prime number (only divisible by itself & 1: "):
	try:
		val = int(user_number)
		print "Good number!"
	except ValueError:
		print "That's a really shitty number. And by shitty number, I mean it's not a number at all."

get_number()
# put all numbers between 1 & user_number into a list

# divide user_number by each number in the list. If you ever have an instance where
# there is no remainder, tell user that the number is Composite (aka not prime)