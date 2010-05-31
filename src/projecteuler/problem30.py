'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
from permutation import produce

def solve(n):
    # It is 999.999 > 9^5 + 9^5 + 9^5 + 9^5 + 9^5
    i=0
    m = range(10)
    
    numbers = []
    for i in range(1,7):
        for digits in produce([m]*i):
            sum_of_fifth_powers = sum([d**n for d in digits])
            number = int("".join([str(d) for d in digits]))
            if number > 1 and number == sum_of_fifth_powers:
                numbers.append(number)
    
    result = sum(set(numbers))
    print("The sum of all the numbers that can be written as the sum of fifth powers of their digits is %(result)d" % vars())

if __name__ == "__main__":
    solve(5)
