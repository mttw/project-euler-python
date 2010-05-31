"""Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

from problem21 import sum_proper_divisors

if __name__ == '__main__':
    # By mathematical analysis, it can be shown that all integers 
    # greater than 28123 can be written as the sum of two abundant numbers
    LIMIT = 28123
        
    map = {}
    for num in range(1, LIMIT + 1):
        divsum = sum_proper_divisors(num)
        # only collect abundandt number
        if (divsum > num):
            map[num] = divsum 

    n_abundant = len(map)
    
    list_ab = map.keys()
    sum_map = {}
    sum_list = []
    for i in range(len(list_ab)):
        for j in range(i, len(list_ab)):
            sum_map[list_ab[i] + list_ab[j]] = 1
    
    
    s = sum(range(LIMIT + 1))
    for ab in sum_map.keys():
        if(ab <= LIMIT):
            s -= ab
            
    result = s
    print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is %(result)d" % vars())
