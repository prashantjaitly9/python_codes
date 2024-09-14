import random

def guessSecret():
    x = int(input("Guess between 0-9: "))
    retval = False
    if x == secret:
        print("Voila!! You guessed right.")
        retval = True
    elif x < secret:
        print("Too less!")
    else:
        print("Too much!")
    return retval

def guessChance(chance):
    while(chance>0):
        if guessSecret():
            return
        else:
            chance-=1


secret = random.randint(0, 9)
print(secret)
guessChance(10)