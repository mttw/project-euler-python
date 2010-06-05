import time

def list_to_dict(l, value):
    m = {}
    for e in l:
        m[e] = value
    return m
    


def find_first_n(f, n, seq):
    """Return first item in sequence where f(item) == True."""
    l = []
    for item in seq:
        if f(item): 
            l.append(item)
            if len(l) == n:
                return l


def find_first(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item): 
            return item

def accumulate(items):
    return reduce(lambda x,y: x+y, items)

def sum_of(items):
    return accumulate(items)

def product_of(items):
    return reduce(lambda x,y: x*y, items, 1)

def measure(f, *args):
    start = time.clock()
    f(args)
    duration = time.clock() - start
    print("Duration: %(duration).3fs" % {'duration': duration})    
    

def boolean_product_of(values):
    return reduce(lambda x,y: x & y, values, True)
