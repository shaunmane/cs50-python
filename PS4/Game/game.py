import random
import sys

def nlevel():
    while True:
        level = input("Level: ")
        if level.isdigit():
            if int(level) == 0:
                pass
            else:
                rnumb = random.randint(1, int(level))
                nguess(rnumb)
                break
        else:
            pass

def nguess(a):
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            if int(guess) > int(a):
                print("Too large!")
                pass
            elif int(guess) < int(a):
                print("Too small!")
                pass
            elif int(guess) == int(a):
                sys.exit("Just right!")
        else:
            pass
nlevel()


