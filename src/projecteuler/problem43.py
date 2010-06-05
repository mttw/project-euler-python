'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In this way, we note the following:

    * d_(2)d_(3)d_(4)=406 is divisible by 2
    * d_(3)d_(4)d_(5)=063 is divisible by 3
    * d_(4)d_(5)d_(6)=635 is divisible by 5
    * d_(5)d_(6)d_(7)=357 is divisible by 7
    * d_(6)d_(7)d_(8)=572 is divisible by 11
    * d_(7)d_(8)d_(9)=728 is divisible by 13
    * d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
from permutation import produce, all_perms
import time
from sets import Set

def subdigits(n , s):
    nstr = str(n)
    return [int(nstr[i:i+s]) for i in range(len(nstr) - s + 1)]

# TODO improve 
        
def solve():
    start = time.clock()
    divisors = [2, 3, 5, 7, 11, 13, 17]
    N = len(divisors)
    pandigitals_with_property = []
    for pandigit in all_perms('0123456789'):
        if pandigit[0] == '0':
            continue
        sds = subdigits(pandigit, 3)
        satisfied = True
        for i in range(N):
            if sds[i+1] % divisors[i] != 0:
                satisfied = False
                break
        if satisfied:
            pandigitals_with_property.append(int(pandigit))
            

    print(pandigitals_with_property)
    result = sum(pandigitals_with_property) #@UnusedVariable
    
    print("The sum of all 0 to 9 pandigital numbers with the substring divisibility property given in problem 43 is %(result)d" % vars())
    print(time.clock()-start)
if __name__ == "__main__":
    solve()
