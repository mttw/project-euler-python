'''
What is the difference between the sum of the squares and the square of the sums?
'''
from projecteuler import sum_of

def sum_of_squares(items):
    return sum_of(map(lambda x: x**2, items))

def square_of_sums(items):
    return sum_of(items)**2


items = range(1,101)
sum1 = sum_of_squares(items)
sum2 = square_of_sums(items)
result = sum2 - sum1
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum" 
      + " is %(sum2)d - %(sum1)d = %(result)d" % vars())
