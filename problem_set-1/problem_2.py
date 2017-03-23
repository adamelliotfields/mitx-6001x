'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
'''

s = 'azcbobobegghakl'

bob_length = len('bob')
string_length = len(s)

number = 0

for i in range(0, string_length-bob_length+1):
    if s[i:i+bob_length] == 'bob':
        number = number + 1

print('Number of times bob occurs is: %s' % number)
