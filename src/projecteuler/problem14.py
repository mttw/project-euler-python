"""Which starting number, under one million, produces the longest chain?"""
import time

def solve(ceiling):
    max = 1
    maxNum = 1
    cache = {}
    for starting_number in range(1, ceiling + 1):
        l = generate_list(starting_number, cache)
        cache[starting_number] = l

        if len(l) > max:
            max = len(l)
            maxNum = starting_number
   
    return cache[maxNum]


def generate_list(starting_number, lists_cache):
    list = [starting_number]
    while starting_number != 1:
        if (starting_number % 2):
            starting_number = 3*starting_number + 1
        else:
            starting_number = starting_number / 2
        
        try:
            known_list = lists_cache[starting_number]
            return list + known_list
        except KeyError, e:
            list.append(starting_number)

    return list 
            


if __name__ == "__main__":
    N = 10**6
    start = time.clock()
    largest_chain = solve(N)
    result = largest_chain[0]
    print("Starting number %(result)d produces the longest chain under %(N)d" % vars())
    duration = time.clock() - start
    print("Duration: %(duration).3fs" % vars())    