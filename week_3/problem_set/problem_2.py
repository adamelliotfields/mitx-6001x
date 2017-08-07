'''
Next, implement the function getGuessedWord() that takes in two parameters - a
string, secretWord, and a list of letters, lettersGuessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in lettersGuessed are in secretWord. This shouldn't be too different
from isWordGuessed()!

For this function, you may assume that all the letters in secretWord and
lettersGuessed are lowercase.
'''


def getGuessedWord(secretWord, lettersGuessed):
    string = ''
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += '_ '
    return string
