#!/usr/bin/env python3

import random
import re

# https://stackoverflow.com/questions/18834636/random-word-generator-python
word_file = "/usr/share/dict/words"
word_list = open(word_file).read().splitlines()

regex = "[a-z]{7,}"  # At least 7 letters, all lower-case (no proper nouns)
tries = 0
while True:
    secret_word = random.choice(word_list)
    tries +=1
    if re.match(regex, secret_word):
        break

#print(secret_word)     # debug
#print(tries)           # debug


def list_to_stretched_string(lst):
    str = ""
    for i in range(len(lst)):
        str += lst[i]
        str += ' '
    return(str)

secret_display = ["_" for i in range(len(secret_word))]
guessed_letters = []
strikes = 0

while strikes < 10 and "_" in secret_display:
    print("")
    print(list_to_stretched_string(secret_display))
    print("Guesses: ", list_to_stretched_string(guessed_letters))
    print("Strikes: ", strikes)

    guess = input("Guess a letter: ")
    guessed_letters.append(guess)
    guessed_letters.sort()
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                secret_display[i] = guess
    else:
        strikes += 1
        print("\nNOPE! Strike ", strikes)

if strikes == 10:
    print("Game over: You got hung")
else:
    print("Game over: You WIN!")

print("The word is", secret_word)

