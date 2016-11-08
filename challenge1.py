# Challenge 1 from http://www.practicepython.org/

# Create a program that asks the user to enter their name and their 
#  age. Print out a message addressed to them that tells them the year 
#  that they will turn 100 years old.

# EXTRAS:

#  Add on to the previous program by asking the user for another number 
#    and printing out that many copies of the previous message. 
#    (Hint: order of operations exists in Python)

#  Print out that many copies of the previous message on separate lines.
#    (Hint: the string "\n is the same as pressing the ENTER button)

user_name = raw_input("What is your name? \n")
user_age = int(raw_input("And how old are you? \n"))

# Validate the age is a valid, positive integer. Promt again if not.
def validateAge(age):
	while user_age =! int:
		print "Please enter a number for your age...\n"
		new_age = int(raw_input("How old are you?\n"))
		return age

# validateAge(user_age)
# print user_age

# Calculate the age from 100.  If over 100, send sassy response.
def whenHundred(user_age):
	if user_age > 100:
		print "You're over 100 eh? Good luck with that..."