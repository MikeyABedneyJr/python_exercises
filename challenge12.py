'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function
'''

def reduce_list():
    #use a counter to get 5 numbers from the user
    count = 0
    number = []
    print "We are going to ask for 5 numbers."
    print "Please use only real integers"

    while count <= 4:
        
        number.append(int(raw_input("Your number is:\n")))
        count += 1

    print "Your first and last digit that you supplied were: ", number[::len(number)-1]
    #reduce_list by some way [1::-1]    

reduce_list()