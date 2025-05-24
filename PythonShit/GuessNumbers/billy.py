import random
import math
from re import A
#random choose a number
rnums = int(input("How many times do i guess a random number?: \n"))


#guesser

def higher(guess, guesses):
    guess = guess + math.ceil(50/(2**guesses))
    #print("too low")
    return(guess)

def lower(guess, guesses):
    guess = guess - math.ceil(50/(2**guesses))
    #print("too high")
    return(guess)

def findit():
    #rnum = 17
    rnum = random.randint(0,100)
    #print(f"the random num is {rnum}")
    guess = 50
    guesses = 0
    while rnum != guess:
        #print(f"guessed {guess}")
        guesses += 1 
        if guess > rnum:
            guess = lower(guess, guesses)
            continue
        if guess < rnum:
            guess = higher(guess, guesses)
            continue
    #print(f"the random number was {rnum}, and we got {guess} in the end")
    return (guesses+1),rnum

i=0
guesseslist = []
rnumlist = []
while i<rnums:
    i +=1
    a,b = findit()
    guesseslist.append(a)
    rnumlist.append(b)
print(guesseslist)
print(rnumlist)
print(f"guessed {len(guesseslist)} numbers, for an average of {(sum(guesseslist))/(len(guesseslist))} tries per guess")