'''
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
...
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''
from number import lsqrt

def f(m,n):
    return ((m*(m+1))/2) * ((n*(n+1))/2) 

def find_n(m, N):
    begin = 2*N/(m*(m+1))
    solutions = []
    for n in range(begin, begin+3):
        solutions.append((n, f(m,n)))
    print(solutions)
    return min(solutions, key=lambda (n,z): abs(z-N))[0]

def solve(N):
    solutions = []
    for m in range(1,2*lsqrt(lsqrt(N))+4):
        n = find_n(m, N)
        solutions.append((m,n, f(m,n)))
        
    print(solutions)
    closest = min(solutions, key=lambda (a,b,z): abs(z-N))
    return closest[0]*closest[1]

if __name__ == "__main__":
    N = 2*10**6
#    N = 60
    result = solve(N)
    print(f(3,1))
    print(f(3,2))
    print(f(3,3))
    print(f(3,4))
    print("The area of the grid with the nearest solution to N = %(N)d is %(result)d" % vars())
