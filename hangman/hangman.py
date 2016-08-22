#!/usr/bin/python
import math
import os
import random
from hangmanpics import get_picture as show_pic

# Creates wordlist from file called 'wordlist'
wordlist = []
with open ('wordlist') as inputfile:
    for i in inputfile:
        i = i[:-1]
        if i[0].islower() and i.isalpha() and len(i)> 3:
            wordlist.append(i)

#Chooses a random word from a list
def get_word(wordlist):
    return random.choice(wordlist)

#Main Screen/"UI"
def show_status(answer, guesses, guessed_letters):
    os.system('clear')
    print show_pic(guesses)+"\n\nWhat is this word?   ", \
    answer +"\n\nYou have %i guesses left\n" %(guesses)
    if len(guessed_letters) > 0:
        print "You have guessed the following letters- ",
        for i in guessed_letters:
            print i + " ",
    print "\n"

#Reset all variables + choose new word
def reset():
    word = get_word(wordlist)
    return (word, "-"*len(word), 7, "", "")

#Get user selected letter
def get_letter(guessed_letters):
    letterChoice = raw_input("Guess a letter:  ").lower()
    while (letterChoice in guessed_letters) or (len(letterChoice) != 1) or not letterChoice.isalpha():
        if (len(letterChoice) != 1):
            letterChoice = raw_input("Please guess ONE letter:  ")
        elif letterChoice in guessed_letters:
            letterChoice = raw_input("You have already guessed %s. Guess another letter:  " %(letterChoice.upper()))
        else:
            letterChoice = raw_input("%s is not a letter. Guess a letter:  " %(str(letterChoice)))
    guessed_letters += letterChoice.lower()
    return letterChoice, guessed_letters


def end_of_game(answer, word, record):
    os.system("clear")
    print show_pic(guesses) + "\n"
    if answer != word:
        print "You lose!\n"
        record[1] += 1
    else:
        print "You win!\n"
        record[0] += 1
    print "The word was " + word.upper()
    print "\nYou have won %i games and lost %i games" %(record[0], record[1])
    scores = open('.hangman_scores','w')
    scores.write(str(record[0]) + ',' + str(record[1]))
    scores.close()
    return raw_input("\nDo you want to play again? (Yes/No)  ")[0].lower()

def get_scores():
    try:
        scorefile = open('.hangman_scores')
        win_loss = scorefile.readline().strip().split(',')
        scorefile.close()
        return [int(win_loss[0]), int(win_loss[1])]
    except IOError:
        return [0, 0]


if __name__ == "__main__":

    while True:
        word, answer, guesses, guessed_letters, letterChoice = reset()
        record = get_scores()
        while guesses > 0 and answer != word:
            show_status(answer, guesses, guessed_letters)
            letterChoice, guessed_letters = get_letter(guessed_letters)

            if letterChoice in word:
                for index in range(0,len(word)):
                    if word[index] == letterChoice:
                        answer = answer[:index] + word[index] + answer[index+1:]
            else:
                guesses -= 1

        if end_of_game(answer, word, record) != "y":
            os.system('clear')
            break
