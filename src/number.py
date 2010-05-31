import math
from projecteuler import sum_of, product_of

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


def is_pandigital(n):
    prev = 0
    for digit in [int(s) for s in sorted(str(n))]:
        if digit - prev != 1:
            return False
        prev = digit
        
    return True


def factorial(n):
    return product_of(range(2,n+1))

def sum_of_digits(num):
    return sum_of([int(d) for d in str(num)])


def lsqrt(number):
    return int(math.sqrt(number))


def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_square(number):
    return number == lsqrt(number)**2


def triangular(i):
    return i*(i-1)/2

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

