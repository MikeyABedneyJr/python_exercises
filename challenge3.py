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

# Start a blank list to populate with the 10 digits a user picks
list = []

# This will be used for the while loop so we only get 10 digits from them
counter = 0


while counter < 10:
    user_number = raw_input("Please give us a number:\n")
	
    # Make sure the input is an integer, if not, ask again & do *not* 
    #  increment our counter
    try:
        val = int(user_number)
        list.append(int(user_number))
        counter = counter + 1
    except ValueError:
        print "Please use integers only."

# Print the list so users will see what they chose before comparing values
print list


def get_less_than_value():
    
    start_value = input("""\nNow tell me a new number and I will tell you which one in your list are smaller. """)
    
    # Check to make sure the user gave you an actual integer
    try:
        start_value = int(start_value)
    except ValueError:
    	print("Soooo, remember we need integers (whole numbers) here.  Try again!")
    	get_less_than_value()

    # Loop through the list and sort into greater than, less than & equal to print statements
    for values in list:
    	if values < start_value:
    		print ("%s is less than %s" % (values, start_value))
        elif values == start_value:
            print ("%s is equal to %s" % (values, start_value))
    	else:
    		print ("%s is MORE than %s" % (values, start_value))

# By this time we will have a list of 10 numbers, now let's run the method to get a
#  second number and we will say what numbers are less than, greater than, or equal
#  to the number they select
get_less_than_value()