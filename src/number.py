import math


def comb(n, r):
    return math.factorial(n)/(math.factorial(r) * math.factorial(n - r))


def triangle_number(n):
    return n*(n+1)/2

def find_triangle_index_below(a):
    return lsqrt(2*a)

def is_triangle_number(a):
    est = find_triangle_index_below(a)
    for n in range(est, est + 3):
        if a == triangle_number(n):
            return True
    
    return False

def is_hexagonal_number(a):
    est = find_hexagonal_index_below(a)
    for n in range(est, est + 2):
        if a == hexagonal_number(n):
            return True
    return False

def find_hexagonal_index_below(a):
    return lsqrt(a/2.0) + 1

def hexagonal_number(n):
    return n*(2*n - 1)


def pentagonal_number(n):
    return n*(3*n - 1) / 2

def find_pentagonal_index_below(a):
    return lsqrt((2.0/3.0)*a)

def is_pentagonal_number(a):
    estimate = find_pentagonal_index_below(a)
    for n in [estimate, estimate + 1]:
        if a == pentagonal_number(n):
            return True
    return False

def circulate(n):
    digits = str(n)
    return [int(digits[i:] + digits[0:i]) for i in range(len(digits))]

def is_prime(n):
    if n <= 1:
        return False
    for d in range(2, lsqrt(n)+1):
        if n % d == 0:
            return False
    return True


def is_pandigital(n, r = None):
    prev = 0
    snum = str(n)
    if r and r != len(snum):
        return False
    for digit in [int(s) for s in sorted(snum)]:
        if digit - prev != 1:
            return False
        prev = digit
        
    return True


def factorial(n):
    return math.factorial(n)

def sum_of_digits(num):
    return sum([int(d) for d in str(num)])


def lsqrt(number):
    return int(math.sqrt(number))


def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_square(number):
    return number == lsqrt(number)**2



def triangulars():
    i = 0
    sum = 0
    while True:
        i += 1
        sum += i
        yield sum

def divisors_of(n):
    divs = [1,n]
    for i in range(2, lsqrt(n) + 1):
        if (n%i) == 0:
            divs += [i, n/i]
    
    if divs[-1] == divs[-2]:
        return divs[:-1]
    else:
        return divs


def square_divisors_of(n):
    square_divs = []
    for i in range(2, lsqrt(n) + 1):
        if (n % i**2) == 0:
            square_divs += [i**2]
    
    return square_divs




def is_triangular_number2(a):
    s = 0
    for i in range(1, a + 1):
        s += i
        print(i, s)
        if a == s:
            return True
        elif s > a:
            return False
    
    return False


