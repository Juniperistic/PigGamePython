#used this tutorial https://youtu.be/21FnnGKSRZo?si=MuGbBqBKqRWSMMJy
#pig game - muiltiplayer game where each player gets a turn to roll a die 
#you can roll a number 1-6 anytime you get a number greater than 1 you add that 
#to your overall score, you can decide how many times to roll the die, anytime you roll a 1 
#you will lose your score and your score will be 0
#example max score will be 50, whenever a player gets 50 they win

#generating a random number 
import random

#define roll function
def roll():
    min_value = 1
    max_value = 6

    #gives a random integer from the minvalue to maxvalue 
    roll = random.randint(min_value, max_value)

    #return's whatever value of roll is to the user who inputted the return function
    return roll

while True:
    players = input("Enter the number of players (2-4): ")

    #if players is equal to a valid whole number
    if players.isdigit():
            #converts the input from a string to an integer
            players = int(players)
            if 2 <= players <= 4:
                #break exits outside of the while loop
                break
            else: print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

#setting up the max scores & player scores
max_score = 50
#a list that contains each of the player's scores
#puts a zero inside the list for every player in the list
#range - loops the number of players 
player_scores = [0 for _ in range(players)]

#simulate each player's turn
#go through the player turns, as long as no player has reached the max score
while max(player_scores) < max_score:

    #loop over each of the players
    for player_idx in range(players):
        #\n adds a line break 
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            #.lower makes it so if the player inputs a capital y it still will roll,
            #because it makes the uppercase into a lowercase y
            if should_roll.lower() != "y": 
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, 
      "is the winner with a score of:", max_score)
