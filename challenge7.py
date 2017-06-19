'''
Write one line of Python that takes a given list and makes a new list that has only the even elements of this list in it. http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
'''

import random
from random import randint


given_list = random.sample(xrange(101),randint(1, 101))
# even_numbers = [number % 2 == 0 for number in given_list]
  # This only prints [false, true, false,...] and not actual values

even_numbers = [number for number in given_list if number % 2 == 0]
 # This says even_numbers = [number] and "number" is determined by all the logic that follows it (i.e the for loop and if statement)

print given_list, "\n\n", even_numbers