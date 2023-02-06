#!/usr/bin/python3
"""A solution for the following problems,

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

"""
def minOperations(n):
    # if it is composite the return true
    # uncompleted
    if n < 1:
        return 0

    store = {'num_of_factors': 0, 'smallest': n}
    for i in range(1, n+1):
 
        current = i + n // i
        if (n // i == n / i):
            store['num_of_factors'] += 1
            if current < store['smallest']:
                store['smallest'] = current
            

    return store['smallest']


if __name__ == '__main__':
    for i in range(0, 100000):
        print(i, ' = ', minOperations(i))

"""
n=1, return current_value = 1
n=2  return -> copy, paste = 2
n=3 return copy, paste, paste = 3
n=4 return copy, paste, paste, paste = 4
    or return copy, paste, copy, paste = 4
n=5 return copy, paste, paste, paste, paste = 5
n=6 return copy, paste, paste, copy, paste = 5
n=7 return copy, paste, paste, paste, paste, paste, paste = 7
n=8 return copy, paste, paste, paste, copy, paste = 6
    or return copy, paste, copy, paste, paste, paste = 6
n=9 return copy, paste, paste, copy, paste, paste = 6
n=10 return copy, paste, paste, paste, paste, copy, paste = 7
n=11 return copy, paste, paste, paste, paste, paste, paste, paste, paste, paste, paste = 11 
n=12 return copy, paste, paste, copy, paste, copy, paste = 7
n=13 return c, p, p, p, p, p, p, p, p, p, p, p, p = 13
n=14 return c, p, p, p, p, p, p, c, p = 9
"""

# composite numbers are numbers that has more than two factors

# while prime numbers are numbers that has two factors and the factors are 1 & the number itself

# 0 - neither p nor c
# 1 - neither p nor c
# 2 - p
# 3 - p
# 4 - c ,...
