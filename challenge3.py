# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of 
# the list that are less than 5.

# EXTRAS:
#
# 1) Instead of printing the elements one by one, make a new
#    list that has all the elements less than 5 from this list
#    in it and print out this new list.
#
# 2) Write this in one line of Python.
#    Ask the user for a number and return a list that contains
#    only elements from the original list a that are smaller 
#    than that number given by the user.

print ("""
Time for a new game. Give me 10 numbers and then I will tell 
you which ones are less than another number...
""")

list = []
counter = 0

while counter < 10:
	user_number = raw_input("Please give us a number:\n")
	try:
		val = int(user_number)
		list.append(user_number)
		counter = counter + 1
	except ValueError:
		print "Please use integers only."
	print list

