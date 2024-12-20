import random

print("You have six guesses to figure out a five letter word")

word_list = ["apple", "berry", "charm", "daisy", "eagle", "happy", "mayor", "green", "alpha", "every", "nicer"]

chosen_word = random.choice(word_list)


for x in range(1,7):
    guess = input("Guess here: ")
    guess = guess.lower()
    

    if guess == chosen_word:
        print("The word is")
        print(chosen_word)
        print("Congrats you win!")
        break
    else:
        for i in range(len(guess)):
            if guess[i] == chosen_word[i]:
                print(f"we have a green letter {guess[i]}")

    
    
    
















# Color to letters



# guesses = []
# guesses.append(guess)

# # guesses now equals ["words"]

# # print each letter and index and index in a word
# for i in range(len(guess)):
#     print(i, guess[i])