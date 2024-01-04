import random

# does a roll of a D6 die
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# prints a table of the scores for each player
def printPlayerScores(player_scores):
    width = 25
    fullLine = (width+2) * '-'
    blankLine = '|' + width * ' ' + '|'
    playerScoreStr = "|     ["
    for item in player_scores:
        if playerScoreStr[-1] != '[':  # if this is first item do not add the comma
            playerScoreStr += ", "
        playerScoreStr += str(item)
    playerScoreStr += ']'
    playerScoreStr += (width +1 - len(playerScoreStr)) * ' '
    playerScoreStr += "|"

    print('\n')
    print(fullLine)
    print(blankLine)
    print("|   Player score Summary  |")
    print(playerScoreStr)
    print(blankLine)
    print(fullLine)

    return

