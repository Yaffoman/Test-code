import random


def new_word():
    with open('newDict.txt', 'r') as f:
            lines = f.readlines()
            return lines[random.randrange(0, len(lines))]


def new_game():
    the_word = new_word().strip()
    print 'Welcome to Hangman!'
    spots = "_" * len(the_word)
    num = 0
    while the_word != len(the_word)*"9":
        print spots
        guess = raw_input('Guess a letter:').upper()
        if guess in the_word.upper():
            while guess in the_word.upper():
                n = the_word.index(guess)
                the_word = the_word[:n] + "9" + the_word[n+1:]
                spots = spots[:n] + guess + spots[n+1:]
        else:
            print 'Wrong!'
            num += 1
            if num > 6:
                print "The word was:\t" + the_word
                return False
    return True

if raw_input("Would you like to play a game(y/n)?\t") == "y":
    if new_game():
        print "Congratulations! \nYou guessed the answer!"
    else:
        print "You Lost :("
    while raw_input("Would you like to play again?(y/n)\t") == "y":
        if new_game() <= 6:
            print "Congratulations! \nYou guessed the answer!"
        else:
            print "You Lost :("
