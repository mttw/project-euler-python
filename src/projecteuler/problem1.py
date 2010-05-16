'''
Add all the natural numbers below one thousand that are multiples of 3 or 5.
'''
from projecteuler import accumulate

def is_multiple_of_3_or_5(number):
    return (number % 3) == 0 or (number % 5) == 0


def solve(ceiling):
    multiples = filter(is_multiple_of_3_or_5, range(1, ceiling))
    return accumulate(multiples)



ceil = 1000
result =  solve(ceil) 

print("The sum of all the multiples of 3 or 5 below %(ceil)d is %(result)d" % vars())
