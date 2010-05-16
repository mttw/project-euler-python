'''
Add all the natural numbers below one thousand that are multiples of 3 or 5.
'''
#from projecteuler import accumulate
from fibonacci import fibonaccis

def is_even(n): 
    return (n % 2 == 0)
    
def solve(ceiling):
    sum = 0
    for fib in fibonaccis():
        if fib > ceiling:
            break
        if is_even(fib):
            sum += fib

    return sum 

limit = 4000000
result = solve(limit)

print("The sum of all the even-valued terms in the Fibonacci sequence " +
        "which do not exceed %(limit)d is %(result)d" % vars())