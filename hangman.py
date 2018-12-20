
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

guess_display = ["_ " for i in range(len(secret_word))]

def print_guess_display():
    display = ""
    for i in range(len(secret_word)):
        display += guess_display[i]
        display += ' '
    print(display)


strikes = 0
guessed_letters = ""


while strikes < 10 and "_ " in guess_display:
    print("")
    print_guess_display()
    print("guesses: ", guessed_letters)
    print("Strikes: ", strikes)

    guess = input("Guess a letter: ")
    guessed_letters += guess
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guess_display[i] = guess
    else:
        strikes += 1
        print("\nNOPE! Strike ", strikes)

if strikes == 10:
    print("Game over: You got hung")
else:
    print("Game over: You WIN!")

print(secret_word)

