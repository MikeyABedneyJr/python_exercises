'''
Write one line of Python that takes a given list and makes a new list that has only the even elements of this list in it. http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
'''
given_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even_numbers = [number % 2 == 0 for number in given_list]
  # This only prints [false, true, false,...] and not actual values

even_numbers = [number for number in given_list if number % 2 == 0]
 # This says even_numbers = [number] and "number" is determined by all the logic that follows it (i.e the for loop and if statement)

print even_numbers