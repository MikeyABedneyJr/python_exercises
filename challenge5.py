"""
http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python
"""
import random
from random import randint


random_list_1 = random.sample(xrange(101),randint(1, 101))
random_list_2 = random.sample(xrange(101),randint(1, 101))

x = list(set(random_list_1).intersection(set(random_list_2)))

print "Here is list 1:\n", random_list_1, "\n\nHere is list 2:\n", random_list_2, "\n\nAnd their intersection is:\n", x