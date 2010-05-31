'''
What is the value of the first triangle number to have over five hundred divisors?
'''

from number import divisors_of

def solve(N):
    result = 0
    n = 1
    size_prev_divisors = 1     
    while(True):
        n += 1
        size_divisors = len(divisors_of(n))
        if size_divisors*size_prev_divisors >= N:
            if len(divisors_of(n*(n-1)/2)) >= N:
                result = n*(n-1)/2
                break
        size_prev_divisors = size_divisors
    
    print("The value of the first triangle number to have over %(N)s divisors is %(result)d" % vars())

if __name__ == "__main__":
    solve(500)
