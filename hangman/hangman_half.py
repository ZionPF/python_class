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

    lettersGuessed = []
    mistakesMade = 0
    availableLetters = ""
    
    # Print : Welcome to the game, Hangman!

    # Print: I am thinking of a word that is X letters long (X is the lenth)


    # While loop : when we still have guesses, keep the loop

        # Print: ---------------------
        
        # Print: You have X guess left (X is the remaining gesses)

        # Print : Available letters : XXXXX (call lettersGuessed to get them)
        
        # Ask: Please guess a letter: (user input guess letter)

        # If: letter already guessed:

            # Print: ops! You've already guessed that letter:

        # Otherwise: (it's a new letter)

            # Get the previous guessed word (use getGuessedWord)

            # Change the letter to lower case string use string.lower()

            # Add the guessing letter to lettersGuessed list

            # Get the new guessed word (use getGuessedWord)

            # Compare the guessed word with previous guessed word (If):
            # If old_guessed == new_guessed: (Not a good guess)
            
                # Print : Oops! That letter is not in my word: XXX
                # XXX is the guessed word

                # Count one mistake

            # Else: (It's a good guess)

                # Print: Good Guess: XXX
                # XXX is the new guessed word
                

            # Check if the word is guessed (use isWordGuessed)

                # Print: Congratulations, you won!

                # Break out of the loop 
    

        # Here goes outside the loop

        # Print: Sorry, you ran out of guesses. The word was else.

        # Print: Here is the secret: XXX (the secret word)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# Load the list of words into the variable wordlist
wordlist = loadWords()

# Choose a secret word
secretWord = chooseWord(wordlist).lower()

# Call hangman() to guess this word
hangman(secretWord)
