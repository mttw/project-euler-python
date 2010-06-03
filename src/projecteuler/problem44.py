'''
Find the pair of pentagonal numbers, P_(j) and P_(k), for which their sum and difference is pentagonal and D = |P_(k) - P_(j)| is minimised; what is the value of D?
'''
from number import pentagonal_number, is_pentagonal_number, find_pentagonal_index_below


def solve():
    minD = 10**10
    j = 1
    while True:
        j += 1
        p_j = pentagonal_number(j)
        #p_k < p_j
        k_start = find_pentagonal_index_below(max(1, p_j - minD)) + 1
        # choose start such that: |p_j - p_k_start |< minD
        if p_j - pentagonal_number(j-1) > minD:
            break 
        for k in range(k_start, j):
            p_k = pentagonal_number(k) 
            diff = p_j - p_k
            if diff < minD and is_pentagonal_number(diff) and is_pentagonal_number(p_k + p_j):
                minD = diff
                print(minD, k, j)
    
    print("The minimal value for D is %(minD)d" % vars())

if __name__ == "__main__":
    solve()
