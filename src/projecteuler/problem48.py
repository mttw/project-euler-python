'''
Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).
'''

def solve():
    n = sum([i**i for i in range(1,1000+1)])
    result = str(n)[-10:]
    print("The last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000) is %(result)s" % vars())

if __name__ == "__main__":
    solve()
