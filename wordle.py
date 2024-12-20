import random

print("You have six guesses to figure out a five letter word")

word_list = ["apple", "berry", "charm", "daisy", "eagle", "happy", "mayor", "green"]

chosen_word = random.choice(word_list)


for x in range(6):
    guess = input("Guess here: ")
    print(x)

    if guess == chosen_word:
        print(chosen_word)
        print("Congrat you win!")
        break
    
    
    
















# Color to letters



# guesses = []
# guesses.append(guess)

# # guesses now equals ["words"]

# # print each letter and index and index in a word
# for i in range(len(guess)):
#     print(i, guess[i])