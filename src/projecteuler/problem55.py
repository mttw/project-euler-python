'''
How many Lychrel numbers are there below ten-thousand?
'''
from number import is_palindrome

def reversed_number(n):
    return int(str(n)[::-1])
    

def lychrel_sequence(n, limit):
    e = n + reversed_number(n)
    i = 1
    while True:
        yield e
        if is_palindrome(e) or i >= limit:
            break
        e += reversed_number(e)
        i += 1


def solve(N, limit):
    limited_results = [list(lychrel_sequence(i, limit))[-1] for i in range(1, N)]
    lychrel_numbers = filter(lambda n: not is_palindrome(n), limited_results)
    return len(lychrel_numbers)

if __name__ == "__main__":
    limit = 50 - 1
    N = 10**4
    result = solve(N, limit)
    
    print("There are %(result)d Lychrel numbers below %(N)d" % vars())
