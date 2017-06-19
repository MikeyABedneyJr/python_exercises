"""
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
user_move = raw_input("Welcome to Rock, Paper Scissors! Please choose one of the following options: \nRock\nPaper\nScissors\n:").lower()

print user_move