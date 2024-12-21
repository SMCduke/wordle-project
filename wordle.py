import random



print("You have six guesses to figure out a five letter word")

word_list = ["apple", "berry", "charm", "daisy", "eagle", "happy", "mayor", "green", "alpha", "every", "nicer"]

chosen_word = random.choice(word_list)


for x in range(1,7):
    guess = input("Guess here: ")
    guess = guess.lower()
    print(chosen_word)

    if guess == chosen_word:
        print("The word is")
        print(chosen_word)
        print("Congrats you win!")
        break
    else:
        for i in range(len(guess)):
            if guess[i] == chosen_word[i]:
                print(f"we have a green letter {guess[i]}")

            elif guess[i] in chosen_word:
                print(f"we have a yellow letter {guess[i]}")

            else:
                print(f"We have a black letter {guess[i]}", end = " ")

                