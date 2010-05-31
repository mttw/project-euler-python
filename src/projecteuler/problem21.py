"""Evaluate the sum of all the amicable numbers under 10000."""

from number import divisors_of, sum_of


def sum_proper_divisors(num):
    sum = 0
    for f in divisors_of(num):
        sum += f
    #remove num form the sum of factors
    sum -= num
    return sum
    

def amicable_pairs(ceil, map):
    # find amicable pairs
    amicable_pairs = []
    for n in range(1, ceil+1):
        if(map[n] in map and n == map[map[n]] and n != map[n]):
            pair = sorted([n, map[n]])
            if(pair not in amicable_pairs):
                amicable_pairs.append(pair)
    return amicable_pairs

if __name__ == '__main__':
    
    prepared_map = {}
    ceil = 10000
    for n in range(1, ceil+1):
        prepared_map[n] = sum_proper_divisors(n) 
    pairs = amicable_pairs(ceil, prepared_map)
    result = sum_of([a+b for (a,b) in pairs])
    
    print("The sum of all the amicable numbers under %(ceil)d is %(result)d" % vars())
