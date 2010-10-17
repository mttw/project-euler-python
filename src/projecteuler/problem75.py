'''
Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
from number import is_square, lsqrt
import time

def solve(L):
    solutions = {}
    for a in range(1, L/4 + 1):
        if a % 100 == 0:
            print(a)
        for b in range(a+1, (L-2*a)/2 + 1):
            absq = a**2 + b**2
            if is_square(absq):
                c = lsqrt(absq)
                try:
                    solutions[a + b + c].append((a,b,c))
                except KeyError, e:
                    solutions[a + b + c] = [(a,b,c)]
    return len(solutions)

if __name__ == "__main__":
    L = 10**5
    start = time.clock()
    result = solve(L)
    print("There are %(result)d rectangles for L <= %(L)d" % vars())
    print(time.clock() - start)
