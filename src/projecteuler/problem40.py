"""
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.

If d_(n) represents the n-th digit of the fractional part, find the value of the following expression:
d_(1) x d_(10) x d_(100) x d_(1000) x d_(10000) x d_(100000) x d_(1000000)
"""
from projecteuler import product_of

if __name__ == '__main__':
    limit = 10**6
    fraction = ""
    for i in range(1, limit):
        fraction += str(i)
        if(len(fraction) > limit):
            break
        
    indexes = [10**i for i in range(7)]    
    result = product_of([int(fraction[i-1]) for i in indexes])
        
    print("The value of the expression in problem 40 is %(result)d" % vars())
        
    