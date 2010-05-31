"""What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from permutation import all_perms
import time
if __name__ == '__main__':

    start = time.clock()
    l = [p for p in all_perms('0123456789')]
    print(time.clock() - start)
    result = sorted(l)[10**6 - 1]
    
    print("The millionth lexicographic permutation of the digits 0..9 is %(result)s" % vars())
