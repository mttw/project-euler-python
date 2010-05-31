'''
Find the value of D <= 1000 in minimal solutions of x for which the largest value of x  is obtained.
'''

from number import is_square, lsqrt, square_divisors_of
from sieve import factorize_with_eratosthenes
import time
'''
Find minimal solution for x such that   
    x^2 - Dy^2 = 1
'''
def find_min_solution(D):
    y = 1
    if(is_square(D)):
        return None
    
    while(True):
        xsq_candidate = D*(y**2) + 1
        if(is_square(xsq_candidate)):
            return (lsqrt(xsq_candidate), y)
        y += 1
            

def solve():
    result = 0 #@UnusedVariable
    D = 1
#    print(find_min_solution(2))
#    print(find_min_solution(3))
#    print(find_min_solution(5))
#    print(find_min_solution(6))
#    print(find_min_solution(7))
    print(find_min_solution(13))
    #print(find_min_solution(117))
    #print(find_min_solution(217))
    #print(factorize_with_eratosthenes(217))
    start = time.clock()
    mp = {}
    for x in range(2, 50000):
        xsq = x**2
        n = xsq - 1
        square_divisors = square_divisors_of(n)
        for ysq in square_divisors:
            D = n/ysq
            if D <= 1000:
                mp[D] = (xsq, ysq)
                
    print(len(mp))
    print(mp.keys()[-10:])
        
    
    
    print("The largest value of x in minimal solutions for D <= %(D)d is %(result)d" % vars())
    print(time.clock()-start)
if __name__ == "__main__":
    solve()
