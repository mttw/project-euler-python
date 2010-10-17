'''
Find the sum of digits in the numerator of the 100^th convergent of the continued fraction for e.
'''
from continuous_fraction import ContinuousFraction
from number import sum_of_digits

def create_e_continuous_fraction(N):
    items = [2,1]
    for k in range(1, N):
        items += [2*k, 1, 1]
    return ContinuousFraction(items)
        
    
def solve(n):
    cfe = create_e_continuous_fraction(n)
    return sum_of_digits(cfe.to_fraction(n).numerator)


if __name__ == "__main__":
    n = 100
    result = solve(n)
    print("The sum of digits in the numerator of the %(n)dth convergent of the continued fraction for e is %(result)d" % vars())
