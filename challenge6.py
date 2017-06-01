'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
user_string = raw_input("Give me any word and I'll tell you if it's a palindrome:  ")

if user_string[:] == user_string[::-1]:
	print("Your word is a palindrome!")
else:
	print("Your word is NOT a palindrome.")