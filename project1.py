from project1_utils import *

max_score = 20

# print the opening instructions
print("\nWelcome to Pig!!\n----------------\n\n")
print("Each player roles a D6 die, adding the rolled number to their score and tries to a total score of", max_score, ".")
print("But - be careful! If you roll a 1 then you BUST and that turn is over (and you do not keep any of your rolls that turn)\n")

# get the number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

player_scores = [0 for _ in range(players)]

# have each player take turns rolling
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\n****************************************")
        print("Player number", player_idx + 1, "turn has just started!")
        print("   Your total score is:", player_scores[player_idx], "\n")
        current_score = 0
        running_total = player_scores[player_idx]

        while True:
            should_roll = input("   Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("   Oh no - you rolled a 1! You BUSTED!")
                current_score = 0
                break
            else:
                current_score += value
                running_total += value
                print("   You rolled a:", value, " for a total of", running_total)

        player_scores[player_idx] += current_score
        print("   Your total score is:", player_scores[player_idx])

    printPlayerScores(player_scores)

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
#print("\nAnd the winner is...\n.\n..\n...\n")
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
print("Yay!!!")
