'''
Write a function called polysum that takes 2 arguments, n and s. This function
should sum the area and square of the perimeter of the regular polygon. The
function returns the sum, rounded to 4 decimal places.
'''

import math

n = int(input('How many sides does your polygon have?: '))
s = int(input('What is the length of each side of your polygon?: '))


def polysum(n, s):
    area = (0.25 * n * (s ** 2)) / (math.tan(math.pi / n))
    perimeter = ((n * s) ** 2)
    total = area + perimeter
    return round(total, 4)


print('Polysum: ' + str(polysum(n, s)))
