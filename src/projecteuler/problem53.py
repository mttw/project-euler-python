'''
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
from number import comb



def solve(N, L):
    values = []
    for n in range(1, N+1):
        values += filter(lambda c: c > L,
                         [comb(n, r) for r in range(1, n+1)])
        
    return values

if __name__ == "__main__":
    N = 100
    L = 10**6
    values = solve(N, L)
    result = len(values)
    
    print("The number of not necessarily distinct values of comb(n,r), for 1 <= n  <= %(N)d, that are greater than %(L)d is %(result)d" % vars())
