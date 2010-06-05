'''
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''
from number import sum_of_digits

def solve(N):
    max_digit_sum = 0
    for a in range(1, N):
        n = 1
        for b in range(1, N):
            n *= a
            max_digit_sum = max(max_digit_sum, sum_of_digits(n))
    return max_digit_sum

if __name__ == "__main__":
    N = 100
    result = solve(N)
    
    print("The maximal digital sum of numbers a^b, where a, b < %(N)d is %(result)d" % vars())
