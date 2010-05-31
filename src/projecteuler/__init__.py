import time

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
    

