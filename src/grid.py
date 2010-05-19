
def consecutive_subsets_of(items, size_of_subset):
    return [ items[i:i+size_of_subset] for i in range(0, len(items) - size_of_subset + 1)]


def is_matrix(grid):
    result = True
    n = len(grid)
    for line in grid:
        result &= (type(line) == list) and (n == len(line))
    return result


def transposed(lists):
    if not lists: 
        return []
    return map(lambda *row: list(row), *lists)

def diag(matrix):
    assert is_matrix(matrix)
    n = len(matrix)
    diags = []
    for i in range(0, n):
        diags.append([matrix[i-j][j] for j in range(0, i+1)])
        
    for j in range(1,n):
        diags.append([matrix[n-i][j+i-1] for i in range(1, n-j+1)])
    return diags


def diag2(matrix):
    m2 = [line[::-1] for line in matrix]
    return diag(m2)
