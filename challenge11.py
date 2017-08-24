# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not. 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions.


# This function will be repeatedly used to get inputs from the user
def get_number(question_to_ask):
	return raw_input(question_to_ask)

def run_prime():
	print "stuff"
	
	# put all numbers between 1 & user_number into a list


	# divide user_number by each number in the list. If you ever have an instance where
	# there is no remainder, tell user that the number is Composite (aka not prime)	


def is_it_a_number(mikey):

	try:
		val = int(mikey)
		print "Good number!"
		run_prime(mikey)

	except ValueError:
		# Ask user for an actual integer and then use that new number in the is_it_a_number function to check validity
		new_number = get_number("That's a really shitty number. And by shitty number, I mean it's not a number at all.\nPlease give an actual number value this time: ")
		is_it_a_number(new_number)

user_number = get_number("Please give me a prime number (only divisible by itself & 1): ")
is_it_a_number(user_number)





