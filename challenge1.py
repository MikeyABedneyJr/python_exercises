# coding= UTF-8
import datetime

name = raw_input('Yo what yo name sucka? ')
age = int(raw_input('Just how ancient are you? '))
now = datetime.datetime.now()

#calculate when a person will be 100 years old by taking the 
#current year, subtracting their current age then adding 100 
#years.

def year_when_100(age):
	when_you_will_be_100 = now.year - age + 99
	return when_you_will_be_100

answer = year_when_100(age)

print "%s, you will be 100 years old in the year %s" % (name, answer)