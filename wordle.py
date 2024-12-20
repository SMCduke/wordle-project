import random

print("You have six guesses to figure out a five letter word")
word_guessed = input("Guess here: ")

word_list = ["apple", "berry", "charm", "daisy", "eagle"]

chosen_word = random.choice(word_list)















# Color to letters


guess = "words"
guesses = []
guesses.append(guess)

# guesses now equals ["words"]

# print each letter and index and index in a word
for i in range(len(guess)):
    print(i, guess[i])