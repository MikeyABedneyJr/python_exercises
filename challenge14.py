'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''


def testing_set():
	test_set = set()
	test_set.add("mikey")
	test_set.add("brent")
	test_set.add("kristin")
	test_set.add("mikey")
	test_set.add("mikey")
	test_set.add("mikey")
	print test_set

testing_set()
