'''
Write one line of Python that takes a given list and makes a new list that has only the even elements of this list in it.
'''
given_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = [number % 2 == 0 for number in given_list]
print even_numbers

# TODO: find a way to print actual number and not [false, true, false...]