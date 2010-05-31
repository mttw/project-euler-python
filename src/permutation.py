
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]



def produce(sets):
    if len(sets) == 1:
        for e in sets[0]:
            yield [e]
    else:
        for e2 in produce(sets[1:]):
            for e in sets[0]:
                yield [e] + e2
