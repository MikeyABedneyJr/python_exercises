# coding= UTF-8
import datetime

name = raw_input('Yo what yo name sucka?\n>')
age = int(raw_input('Just how ancient are you?\n>'))
rub_it_in_number = int(raw_input('How many times do I need to remind you of the answer?\n>'))
now = datetime.datetime.now()

"""
calculate when a person will be 100 years old by taking the 
current year, subtracting their current age then adding 100 
years.
"""

def year_when_100(age):
	when_you_will_be_100 = now.year - age + 99
	return when_you_will_be_100

answer = year_when_100(age)

print ("%s, you will be 100 years old in the year %s\n" % (name, answer))*rub_it_in_number

"""
1. Add on to the previous program by asking the user for another 
number and printing out that many copies of the previous 
message. (Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate 
lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
