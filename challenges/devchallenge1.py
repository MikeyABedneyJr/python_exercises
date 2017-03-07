# coding= UTF-8
# read file from /usr/share/dict/ --> memory
with open('/usr/share/dict/words', 'r') as dictionary_file:
    dictionary = dictionary_file.read()
    print dictionary
# read stdin

# scan/match letter by letter

# if more than 4 characters match, store suggestion into 
#  function. Display function to user as 
#  recommendations for changed spellings

# Test words:
	# Case (upper/lower) errors: "inSIDE" => "inside"
	# Repeated letters: "jjoobbb" => "job"
	# Incorrect vowels: "weke" => “wake"

