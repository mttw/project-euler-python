import time

def accumulate(items):
    return reduce(lambda x,y: x+y, items)


def measure(f, *args):
    start = time.clock()
    f(args)
    duration = time.clock() - start
    print("Duration: %(duration).3fs" % {'duration': duration})    
    
