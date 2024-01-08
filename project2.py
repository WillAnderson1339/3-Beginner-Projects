from project2_utils import *


# open story and read contents
with open("story.txt", "r") as f:
    the_story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# enumerate through the story characters looking for the target start/end chars
for i, char in enumerate(the_story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = the_story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# for each word in the words list prompt the user for a value and store it in a dictionary
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    the_story = the_story.replace(word, answers[word])

print(the_story)

countStoryLetterFrequeny(the_story, vowel_frequency, letter_frequency)

printLetterFrequency(vowel_frequency, letter_frequency)

