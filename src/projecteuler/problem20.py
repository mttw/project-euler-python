"""Find the sum of the digits in the number 100!"""
from number import sum_of_digits, factorial

if __name__ == '__main__':
    n = 100
    result = sum_of_digits(factorial(n))
    print("The sum of the digits in the number %(n)d! is %(result)d" % vars())
   
    