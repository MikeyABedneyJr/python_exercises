"""
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the 
number is even or odd, print out an appropriate message 
to the user. Hint: how does an even / odd number react 
differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a 
different message.

2. Ask the user for two numbers: one number to check 
(call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""

# coding= UTF-8
user_number = int(raw_input("Pick a numba' any numba':\n"))

def even_or_odd(number):
	if (number % 2 == 0):
		print "Your number is EVEN!"
		if (number % 4 == 0):
			print "Your number is also divisible by 4. LUCKY YOU!!!"
	else:
		print "Your number is ODD!"

even_or_odd(user_number)

# Extra 2 task:
num1 = int(raw_input("""
Bonus round: let's work on dividing two numbers.\n\n
Give me a number to be divided:\n
"""))
num2 = int(raw_input("Give me a number to divide by:\n"))

def bonus_even_or_odd(num1, num2):
	if (num1 % num2 == 0):
		print "Your numbers are evenly divided!"
	else:
		print "Your numbers do not divide evenly"

bonus_even_or_odd(num1, num2)