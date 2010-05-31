'''
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def solve(n):
    # 1x1 -> 1
    # 3x3 -> 25
    # 5x5 -> 101
    # nxn:
    
    s = 1
    result = s
    for i in range(3, n+1, 2):
        result += 4*s + (i-1)*10
        s += 4*(i-1)
           
    print("The sum of the numbers on the diagonals in a 1001 by 1001 spiral is %(result)d" % vars())

if __name__ == "__main__":
    solve(1001)
