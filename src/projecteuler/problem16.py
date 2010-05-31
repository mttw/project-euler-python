"""What is the sum of the digits of the number 2^1000"""
from number import sum_of_digits

if __name__ == '__main__':
    exp = 1000
    result = sum_of_digits(2**exp)
    print("The sum of the digits of 2^%(exp)d is %(result)d" % vars())
   
    