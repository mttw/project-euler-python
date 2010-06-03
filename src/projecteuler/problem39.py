'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''
from number import lsqrt, is_square

from math import sqrt
def perimeter(a, b):
    c = lsqrt(a**2 + b**2)
    
    return a + b + c

def solve(N):
    result = 0 #@UnusedVariable
    perimeter_to_sides = {}
    for a in range(1, N + 1):
        for b in range(a, N-a + 1):
            if is_square(a**2 + b**2):
                p = perimeter(a, b)
                if p > N:
                    break
                c = lsqrt(a**2+b**2)
                try:
                    perimeter_to_sides[p].append((a,b,c))
                except KeyError, e:
                    perimeter_to_sides[p] = [(a,b,c)]


    l = [(p, len(solutions)) for (p, solutions) in perimeter_to_sides.items()]
    r = max(l, key=lambda x:x[1])
    result = r[0] 
    solutions = r[1]
    
    print("The number of solutions is maximised for value p = %(result)d (where p <= 1000) with %(solutions)d solutions" % vars())

    
if __name__ == "__main__":
    solve(1000)
