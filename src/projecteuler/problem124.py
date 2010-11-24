'''
If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
'''


from sieve import sieve_eratosthenes
from prime import factorizations_below


def product_of(items):
    return reduce(lambda x,y: x*y, items, 1)

def rad(factors):
    return product_of([p for (p,e) in factors])

def num(factors):
    return product_of([p**e for (p,e) in factors])

def cmp_rad(tuple1, tuple2):
    (n1, radical1) = tuple1
    (n2, radical2) = tuple2
    return cmp(radical1, radical2) or cmp(n1, n2)

def solve(D, i):
    primes = sieve_eratosthenes(D)
    l = list(factorizations_below(D, primes)) + [((1,1),)]
    E = sorted([(num(factors), rad(factors)) for factors in l], cmp_rad)
    return E[i-1][0]

if __name__ == "__main__":
    D = 10**5
    i = 10**4
    result = solve(D, i)
    
    print("If rad(n) is sorted for 1 <= n <= %(D)d, E(%(i)d)=%(result)d." % vars())
