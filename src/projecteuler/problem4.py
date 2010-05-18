'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''
from number import is_palindrome

       
def solve(therange):
    max_palindrome = 0
    for i in therange:
        for j in range(i, therange[-1] + 1):
            candidate = i*j
            if is_palindrome(candidate) and candidate > max_palindrome:
                max_palindrome = candidate 
            
    return max_palindrome



result = solve(range(100, 1000))
print("The largest palindrome made from the product of two 3-digit numbers " 
      + "is %(result)d" % vars())
