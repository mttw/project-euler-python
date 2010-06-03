'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
...

It can be verified that T_(285) = P_(165) = H_(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
from number import is_hexagonal_number, is_pentagonal_number, triangulars, triangle_number, find_triangle_index_below
from projecteuler import find_first

def solve(T):
    return find_first(lambda n: is_pentagonal_number(n) and is_hexagonal_number(n) and n > T, triangulars())

if __name__ == "__main__":
    result = solve(triangle_number(285))
    index = find_triangle_index_below(result)
    print("The next matching triangle number is T_(%(index)d)=%(result)d " % vars())
