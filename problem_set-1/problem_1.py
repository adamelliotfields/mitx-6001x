'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
'''

s = 'azcbobobegghakl'
vowels = 0

for letter in s:
    if letter in 'aeiou':
        vowels = vowels + 1

print('Number of vowels: %s' % vowels)
