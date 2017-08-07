'''
Write a program that prints the longest substring of s in which the letters
occur in alphabetical order.
'''

import string

s = 'azcbobobegghakl'

index = s[0]
substring = ''

for i in range(1, len(s)):
    if s == string.ascii_lowercase:
        substring = s
    if len(index) > len(substring):
        substring = index
    if s[i] >= s[i-1]:
        index = index + s[i]
    else:
        index = s[i]

print('Longest substring in alphabetical order is: %s' % substring)
