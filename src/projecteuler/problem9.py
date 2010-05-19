'''
Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.
'''
from number import is_square, lsqrt
def solve(n):
    
    for a in range(0, int(n/2) + 1):
        asq = a**2
        start = max(a+1, n/2 - a)
        end = n/2
        for b in range(start, end + 1):
            bsq = b**2
            csq_candidate = asq + bsq
            if(is_square(csq_candidate) and csq_candidate > bsq):
                c = lsqrt(csq_candidate)
                if((a + b + c) == n):
                    return (a, b, c)
        
    return None
       
(a,b,c) = solve(1000)
print("The only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000" 
      + " is (%(a)d, %(b)d, %(c)d)" % vars())
print("Its product abc is " + str(a*b*c))
