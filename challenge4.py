"""
Create a program that asks the user for a number and then prints out a 
list of all the divisors of that number. 
"""

list = []



def get_user_number(user_integer):
  
  x = range(1, user_integer)

  for elem in x:
    if (user_integer % elem == 0):
      list.append(elem)
  
  # Added so that the user number will actually appear in the list of answers.
  list.append(user_integer)

def is_number_an_integer():
  user_number = raw_input("Give me a whole number and I will tell you what numbers will divide into it evenly\n:")

  try:
    user_integer = int(user_number)
    get_user_number(user_integer)
  except ValueError:
    print "You did not enter a whole number.\n\n\n"
    is_number_an_integer()


is_number_an_integer()

print list