#!/usr/bin/env python
"""How many routes are there through a 20 x 20 grid?"""


def solve(m, n, cache):
    sum = 0
    if (n==1):
        return m+1
    elif (m,n) in cache:
        return cache[(m,n)]
    
    for i in range(1, m + 1):
        sum += solve(i, n-1, cache)
    
    sum +=1
    cache[(m,n)] = sum

    return sum

if __name__ == '__main__':
    (m, n) = (20, 20)
    result = solve(m, n, {})
    print('There are %(result)d routes through a %(m)d x %(n)d grid' % vars())
    
    
