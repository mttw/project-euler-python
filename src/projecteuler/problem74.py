'''
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
from math import factorial
from itertools import count

class Chain:
    def __init__(self, starting_number, limit=10**6):
        prev = starting_number
        mp = {}
        elements = []
        loop_start_index = None
        for i in range(0, limit):
            mp[prev] = i
            elements.append(prev)
            next = sum_digits_factorials(prev)
            if next in mp:
                loop_start_index = mp[next]
                break
            prev = next
        
        if loop_start_index == None:
            raise ValueError("Chain not finished before reaching element count " + str(limit))
        self.start = elements[:loop_start_index]
        self.chain = elements[loop_start_index:]

    def __repr__(self):
        return 'Chain(' + str(self)[1:-2] + ')'
        
    def __str__(self):
        msg = ", ".join([str(n) for n in self.start])
        if len(msg) > 0:
            msg += ', ' 
        return '[' +  msg + '(' + ", ".join([str(n) for n in self.chain]) + ')]' 

def digits(n):
    return [int(digit) for digit in str(n)]

def sum_digits_factorials(n):
    return sum([factorial(d) for d in digits(n)])



def solve(w, N):
    l = []
    for i in range(1, N):
        if i % 10000 == 0:
            print(i)
        try:
            c = Chain(i, w)
            if len(c.start) + len(c.chain) == w:
                l.append(c)
        except Exception, e:
            print(e)
    return len(l)

if __name__ == "__main__":
    w = 60
    N = 10**6
    result = solve(w, N)
#    print(sum_digits_factorials(145))
    print("There are %(result)d chains, with a starting number below one million, contain exactly %(w)d non-repeating terms." % vars())
