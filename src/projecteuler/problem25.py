'''
What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
from fibonacci import fibonacci
from itertools import count

def solve():
    for i in count(1):
        fib = fibonacci(i)
        if(len(str(fib)) >= 1000):
            return i #@UnusedVariable
    

if __name__ == "__main__":
    result = solve()
    print("The first term in the Fibonacci sequence to contain 1000 digits is %(result)d" % vars())