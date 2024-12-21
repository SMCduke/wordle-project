import random

from datetime import datetime

__author__ = 'aGn'
__copyright__ = "Copyright 2021, Planet Earth"


class ColoredPrint:
    def __init__(self):
        self.PINK = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'

    def __call__(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.msg, **kwargs)
        return self

    def disable(self):
        self.PINK = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def store(self, *args, path: str = 'logfile.log'):
        if args:
            self.msg = ' '.join(map(str, args))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(path, mode='a') as file_:
            file_.write(f"{self.msg} -- {date}")
            file_.write("\n")

    def success(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKGREEN + self.msg + self.ENDC, **kwargs)
        return self

    def info(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKBLUE + self.msg + self.ENDC, **kwargs)
        return self

    def warn(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.WARNING + self.msg + self.ENDC, **kwargs)
        return self

    def warning(self, *args, **kwargs):
        return self.warn(*args, **kwargs)

    def err(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.FAIL + self.msg + self.ENDC, **kwargs)
        return self

    def error(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def critical(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def pink(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.PINK + self.msg + self.ENDC, **kwargs)
        return self

    def green(self, *args, **kwargs):
        return self.success(*args, **kwargs)

    def red(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def blue(self, *args, **kwargs):
        return self.info(*args, **kwargs)

    def yellow(self, *args, **kwargs):
        return self.warn(*args, **kwargs)


log = ColoredPrint()

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

                