# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    ret = True
    for i in secretWord:
        if i not in lettersGuessed:
            ret = False
    return ret

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ret = ""
    for i in secretWord:
        if i in lettersGuessed:
            ret += i
        else:
            ret += "_"
    return ret




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    ret = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in lettersGuessed:
            ret += i
    return ret



def giveHint(secretWord,lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    tobe_guessed = []
    tobe_wrong = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    for i in alphabet:
#        if i not in lettersGuessed:
#            tobe_guessed.append(i)
#    for i in tobe_guessed:
#        if i not in secretWord:
#            tobe_wrong.append(i)
#    h = random.choice(tobe_wrong)
#    return h

## Another way:
    while True:
        random_letter = random.choice(list(alphabet))
        print('Hint letter:',random_letter)
        if random_letter not in secretWord and random_letter not in lettersGuessed:
            return random_letter




def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")

    lettersGuessed = []
    mistakesMade = 0
    availableLetters = ""

    while mistakesMade<8:
        print("-------------")
        print("You have", 8-mistakesMade, "guesses left.")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        old_guessed = getGuessedWord(secretWord, lettersGuessed)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:",old_guessed)
        else:
            lettersGuessed.append(guess)
            new_guessed = getGuessedWord(secretWord, lettersGuessed)
            if new_guessed == old_guessed:
                print("Oops! That letter is not in my word:",new_guessed)
                mistakesMade += 1
                hint_letter = giveHint(secretWord, lettersGuessed)
                print("I will give you a hint, there is no: " + hint_letter)
                lettersGuessed.append(hint_letter)
            else:
                print("Good guess:",new_guessed)
            if isWordGuessed(secretWord, lettersGuessed):
                break
        
    print("------------")
    if mistakesMade ==8:
        print("Sorry, you ran out of guesses. The word was else.")
        print(secretWord)
    else:
        print("Congratulations, you won!")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
