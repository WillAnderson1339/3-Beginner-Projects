# dictionary with key = letter; and value a tuple of English letter frequency (Googled), story letter frequency (calculated)
vowel_frequency = {
    "A": [8.167, 0],
    "E": [12.702, 0],
    "I": [6.966, 0],
    "O": [7.507, 0],
    "U": [2.758, 0],
    "Y": [1.974, 0],
}

# dictionary with key = letter; and value a tuple of English letter frequency (Googled), story letter frequency (calculated)
letter_frequency = {
    "B": [1.492, 0],
    "C": [2.782, 0],
    "D": [4.253, 0],
    "F": [2.228, 0],
    "G": [2.015, 0],
    "H": [6.094, 0],
    "J": [0.253, 0],
    "K": [1.772, 0],
    "L": [4.025, 0],
    "M": [2.406, 0],
    "N": [6.749, 0],
    "P": [1.929, 0],
    "Q": [0.095, 0],
    "R": [5.987, 0],
    "S": [6.327, 0],
    "T": [9.056, 0],
    "V": [0.978, 0],
    "W": [2.360, 0],
    "X": [0.250, 0],
    "Z": [0.074, 0],
}

def countStoryLetterFrequeny(story, vowelList, letterList):

    # loop through the story letters counting the number of each letter
    totalLetters = 0

    for i, char in enumerate(story):
        char = char.upper()
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            totalLetters += 1
            if (char in vowelList):
                vowelList[char][1] += 1
            elif (char in letterList):
                letterList[char][1] += 1

    # divide the count by the nuber of letter to create a per centage
    for item in vowelList:
        vowelList[item][1] = vowelList[item][1] / totalLetters * 100
    for item in letterList:
        letterList[item][1] = letterList[item][1] / totalLetters * 100

    return

def printLetterFrequency(vowelFrequency, letterFrequency):

    '''
    # unicode values from https://en.wikipedia.org/wiki/List_of_Unicode_characters

    symbs = [u'\u2502', u'\u2503', u'\u2550', u'\u2551', u'\u2554', u'\u2557', u'\u255a', u'\u255d', u'\u2560', u'\u2566', u'\u2567', u'\u2562', u'\u255f']
    for sym in symbs:
        print(sym)
    print("looping...")
    i = 0
    while i < len(symbs):
        x = hex(symbs[i])
       print(x)
        i += 1

    print("╔═══════╗")
    print("║ A ┃ B ║")
    print("╟═══════╢")
    print("╚═══════╝")
    '''

    printFrequency(vowelFrequency)
    printFrequency(letterFrequency)

    return

def printFrequency(frequency):

    lineTwo    = "║ English frequency "
    lineThree  = "║ Story frequency   "
    numCols = len(frequency)
    numDigits = 2   # number of digits to round to
    width = len(lineTwo) + numCols * (5 + numDigits) +(numCols - 1)

    topLine = "╔" + (width+1) * u'\u2550' + "╗"
    bottomLine = "╚" + (width+1) * u'\u2550' + "╝"
    letterLine = "║ Letter          "
    middleLine = "╟" + (width+1) * u'\u2501' + "╢"


    for key in frequency:
        engFrequency = '{0:.2f}'.format(frequency[key][0])
        if frequency[key][0] < 10:
            engFrequencyStr = " " + str(engFrequency)
        else:
            engFrequencyStr = str(engFrequency)

        storyFrequency = '{0:.2f}'.format(frequency[key][1])
        if frequency[key][1] < 10:
            storyFrequencyStr = " " + str(storyFrequency)
        else:
            storyFrequencyStr = str(storyFrequency)

        letterLine += "   ┃   " +  key
        lineTwo    += " ┃ " + engFrequencyStr
        lineThree  += " ┃ " + storyFrequencyStr
    letterLine += "   ║ "
    lineTwo    += " ║ "
    lineThree  += " ║ "

    print("\nLetter Distribution %\n")
    print(topLine)
    print(letterLine)
    print(middleLine)
    print(lineTwo)
    print(middleLine)
    print(lineThree)
    print(bottomLine)

    return

