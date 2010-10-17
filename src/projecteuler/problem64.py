'''
How many continued fractions for N <= 10000 have an odd period?
'''
from continuous_fraction import ContinuousFraction
import time

    
def solve(N):
    cfs = []
    for n in range(2,N+1):
        if n % 1000 == 0:
            print("N=" + str(n))
        cfs.append(ContinuousFraction.from_sqrt(n)) 
    return len(filter(lambda cf: len(cf.period) % 2 == 1,cfs))

if __name__ == "__main__":
    N = 10000
    start = time.clock()
    result = solve(N)
    print("The number of continued fractions for N <= %(N)d that have an odd period is %(result)d" % vars())
    print(time.clock() - start)