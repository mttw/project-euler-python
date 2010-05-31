'''
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
'''

from number import is_pandigital
from math import log

def solve():
    #     log_10(a) + log_10(b) + log_10(c) <= 9
    # ==> 2*log_10(ab) <= 9
    # ==> log_10(b) <= 4.5 - log_10(a)
    
    pandigital_products = []
    for a in range(1, int(4.5**10)+1):
        for b in range(1, int((4.5**10)/a)+1):
            c = a*b
            pandigital_candidate = str(a)+str(b)+str(c)
            if len(pandigital_candidate) == 9 and is_pandigital(pandigital_candidate):
                pandigital_products.append((a, b, c))
                
    print(pandigital_products)
    result = sum(set([c for (a,b,c) in pandigital_products])) #@UnusedVariable
    
    print("The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is %(result)d" % vars())

if __name__ == "__main__":
    solve()
