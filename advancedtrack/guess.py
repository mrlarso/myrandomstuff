import random

def new_game():
    return random.choice(range(1,1000)), 10


while True:
    number, guesses = new_game()
    while guesses > 0:
        print "Guesses left-  %i" %(guesses)
        guess = input("Choose a number  ")
        guesses -= 1
        if guess == number:
            break
        if guess > number:
            print "Too high!"
        if guess < number:
            print "Too low!"

    if guess == number:
        print "You are a genius. The answer is " + str(number)
    else:
        print "You are not a genius. the answer was " + str(number)

    if raw_input("Do you want to play again (yes/no)?  ")[0].lower() == 'n':
        break
