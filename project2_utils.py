vowel_frequency = {
    "A": [8.167, 0],
    "E": [12.702, 0],
    "I": [6.966, 0],
    "O": [7.507, 0],
    "U": [2.758, 0],
    "Y": [1.974, 0],
}

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


def printLetterFrequency(vowelFrequency, letterFrequency):

    '''
    symbs = [u'\u2502', u'\u2503', u'\u2550', u'\u2551', u'\u2554', u'\u2557', u'\u255a', u'\u255d', u'\u2560', u'\u2566', u'\u2567', u'\u2562', u'\u255f']
    for sym in symbs:
        print(sym)
    print("looping...")
    '''
    '''
    i = 0
    while i < len(symbs):
        x = hex(symbs[i])
       print(x)
        i += 1
    '''
    #print("╔═══════╗")
    #print("║ A ┃ B ║")
    #print("╟═══════╢")
    #print("╚═══════╝")

    #countStoryLetterFrequeny(vowel_frequency, letter_frequency)

    lineTwo    = "║ English frequency "
    lineThree  = "║ Story frequency   "
    numCols = len(vowelFrequency)
    numDigits = 2   # number of digits to round to
    width = len(lineTwo) + numCols * (4 + numDigits) +4

    topLine = "╔" + (width+2) * u'\u2550' + "╗"
    bottomLine = "╚" + (width+2) * u'\u2550' + "╝"
    headerLine = "║ Letter           "
    middleLine = "╟" + (width+2) * u'\u2501' + "╢"


    for key in vowelFrequency:
        engFrequency = '{0:.2f}'.format(vowelFrequency[key][0])
        if vowelFrequency[key][0] < 10:
            engFrequencyStr = str(engFrequency)
        else:
            engFrequencyStr = " " + str(engFrequency)

        storyFrequency = '{0:.2f}'.format(vowelFrequency[key][1])

        headerLine += "  ┃   " +  key
        #lineTwo    += " ┃ " + str(engFrequency)
        lineTwo    += " ┃ " + engFrequencyStr
        lineThree  += " ┃ " + str(storyFrequency)
    headerLine += "  ║ "
    lineTwo    += " ║ "
    lineThree  += " ║ "

    print("\nLetter Distribution %\n")
    print(topLine)
    print(headerLine)
    print(middleLine)
    print(lineTwo)
    print(middleLine)
    print(lineThree)
    print(bottomLine)

    return

