'''
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
from permutation import is_permuted
from itertools import count

def solve(N):

    for x in count(1):
        all_permuted = True
        for n in [i*x for i in range(2, N+1)]:
            if not is_permuted(n, x):
                all_permuted = False
                break
        if all_permuted:
            return x

if __name__ == "__main__":
    N = 6
    result = solve(N)
    print([i*result for i in range(1, N+1)])
    print("The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits is %(result)d" % vars())
