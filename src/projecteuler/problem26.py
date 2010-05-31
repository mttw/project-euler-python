"""Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""


def ufrac(d):
    (q,r) = (0,1)
    while(1):
        (q,r) = (10*r / d, 10*r % d)
        yield (q,r)
        if(r == 0):
            break

def ufrac_limit(d, limit=10**10):
    i = 0
    l = []
    for d in ufrac(d):
        if(i >= limit):
            break
        elif(d in l):
            w = l.index(d)
            l2 = []
            for e in l:
                l2.append(e[0])
            return [l2[0:w], l2[w:len(l)]]
        l.append(d)
        i += 1
        
    return [zip(*l)[0]]


def str_fraction(list):
    s = "0."
    for a in list[0]:
        s += str(a)
        
    if(len(list)> 1 and len(list[1]) > 0):
        s += "("
        for b in list[1]:
            s += str(b)
        s += ")"
    return s
         

if __name__ == '__main__':
    limit = 1000
    (result, max_length) = (0, 0)
    for d in range(2,limit):
        a=ufrac_limit(d)
        if(len(a) > 1 and len(a[1]) > max_length):
            (result, max_length) = (d, len(a[1]))
        print("1/" + str(d) + ": " + str_fraction(a))

    print("The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is %(result)d (with cycle length %(max_length)d)" % vars())

