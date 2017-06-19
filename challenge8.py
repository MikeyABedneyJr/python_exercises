"""
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
game_on = True

while (game_on == True):
	user_move = raw_input("Welcome to Rock, Paper Scissors! Please choose one of the following options: \nRock\nPaper\nScissors\n:").lower()
	print user_move

	game_on == False

	print game_on

### TODO: Just use BREAK as instructed to stop this forever while loop

# Check that spelling/word is one of the 3 options
  # Make a list ot check against

# Set rules of what beats what

# Randomly generate computer's move/choice

# Check who wins/loses

# Ask to play again