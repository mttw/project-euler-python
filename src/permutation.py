def is_permuted(num, ref):
    return sorted(str(num)) == sorted(str(ref))



def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]



def product(args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def produce(sets):
    if len(sets) == 1:
        for e in sets[0]:
            yield [e]
    else:
        for e2 in produce(sets[1:]):
            for e in sets[0]:
                yield [e] + e2
