'''
First, implement the function isWordGuessed() that takes in two parameters - a
string, secretWord, and a list of letters, lettersGuessed. This function
returns a boolean - True if secretWord has been guessed (ie, all the letters of
secretWord are in lettersGuessed) and False otherwise.

For this function, you may assume that all the letters in secretWord and
lettersGuessed are lowercase.
'''


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True
