"""Find the maximum total from top to bottom of the triangle below"""

t18 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def calc_cost(path, triangle):
    i = 0
    cost = 0
    for entry in path:
        cost += triangle[i][entry]
        i=i+1
    return cost
    

def max_cost(triangle):   
    i = 0
    pathlist = []
    
    for i in range(len(triangle)):
        line = triangle[i]
        nextpathlist = []
        maxCost = 0
        for k in range(len(line)):
            if(k > 0):
                path1 = pathlist[k-1]
            else:
                path1 = []
    
            if(k < len(line) - 1):
                path2 = pathlist[k]
            else:
                path2 = []
                
            
            if(calc_cost(path1, triangle) > calc_cost(path2, triangle)):
                expensive_path = path1[:]
            else:
                expensive_path = path2[:]
            
            expensive_path.append(k)
            cost = calc_cost(expensive_path, triangle)
            maxCost = max(cost, maxCost) 
            nextpathlist.append(expensive_path)
        
        pathlist = nextpathlist[:]
        
    return maxCost
    

def read_triangle(tr):
    return [[ int(n) for n in l.split(" ")] for l in tr.split("\n")]

def solve(triangle):
    result = max_cost(triangle) #@UnusedVariable
    print("The maximum total from top to bottom of the triangle is %(result)d" % vars())


if __name__ == '__main__':
    solve(read_triangle(t18))
