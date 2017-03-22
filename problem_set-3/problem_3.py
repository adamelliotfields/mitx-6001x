'''
Next, implement the function getAvailableLetters() that takes in one parameter
- a list of letters, lettersGuessed. This function returns a string that is
comprised of lowercase English letters - all lowercase English letters that are
not in lettersGuessed.

Note that this function should return the letters in alphabetical order.

For this function, you may assume that all the letters in lettersGuessed are
lowercase.
'''


def getAvailableLetters(lettersGuessed):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    string = ''
    for i in lettersGuessed:
        if i in letters:
            letters.remove(i)
    for j in letters:
        string += j
    return string
