'''
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from number import is_pandigital
#def find_largest_factorial_below(N):
#    i = 1
#    fact = 1
#    while True:
#        i += 1 
#        fact = fact*i
#        if fact > N:
#            return (i-1, fact/i)


def concatenated_product(n, rng):
    return int("".join([str(n*i) for i in rng]))

def solve():
    result = 0 #@UnusedVariable
    pandigital_concatenated_products = []
    # since n > 1, 5 digits are enough
    for m in range (1,10**5):
        for n in range(1,10):
            p = concatenated_product(m, range(1, n+1))
            if len(str(p)) > 9:
                break
            if is_pandigital(p, 9):
                pandigital_concatenated_products.append(p)
            
    
    result = sorted(pandigital_concatenated_products)[-1]
    print("The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1 is %(result)d" % vars())

if __name__ == "__main__":
    solve()
