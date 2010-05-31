
'''
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''

from number import is_palindrome
from math import log

def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def solve(N):
    result = 0 #@UnusedVariable
    palindromes = []
    for i in range(1, N):
        if is_palindrome(i) and is_palindrome(int(int2bin(i))):
            palindromes.append(i) 
        
    result = sum(palindromes)
    print("The sum of all numbers, less than %(N)d, which are palindromic in base 10 and base 2 is %(result)d" % vars())

if __name__ == "__main__":
    solve(10**6)
