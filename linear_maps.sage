def linear_mapf(boolf, A):
    """
    Given the `BooleanFunction` `boolf` and the `GF(2)` matrix $A$, the function `linear_mapf` returns the function $x \mapsto \mathtt{boolf}(A x)$, where $x$ is a positive integer, and its binary expansion is used in the `GF(2)` matrix multiplcation by $A$.
    """
    m = boolf.nvariables()
    return lambda x: boolf(list(A * vector(base2(m, x),GF(2))))

def list_to_int(blist):
    """
    Given the list `blist` representing the binary expansion of a positive integer $n$, the function `list_to_int` returns $n$.
    """
    return sum([blist[k] * 2 ** k for k in xrange(len(blist))])

def enumerate_linear_maps(boolf, certify=False):
    """
    Given the `BooleanFunction` `boolf`, the function `enumerate_linear_maps` returns a list of unique truth tables obtained by enumerating all Boolean functions of the form `linear_mapf(boolf,A)`,
    where $A$ is a matrix in the general linear group `GL(m, GF(2))`.

    The optional parameter `certify` defaults to `False`. If `certify` is true then the function `enumerate_linear_maps` prints each value of $c$ and $A$ for which `linear_mapf(boolf,A) == mapf(boolf,b,c,boolf(b))`,
    that is, $\mathtt{boolf}(A x) = \mathtt{boolf}(x+b) + \langle c, x \rangle + \mathtt{boolf}(b)$.
    """
    m = boolf.nvariables()
    v = 2 ** m
    mapped_ittdict = {}
    if certify:
        for b in xrange(v):
            for c in xrange(v):
                mapped_f = mapf(boolf, b, c, boolf(b))
                mapped_tt = [mapped_f(x) for x in xrange(v)]
                mapped_itt = list_to_int(mapped_tt)
                if mapped_itt in mapped_ittdict:
                    mapped_ittdict[mapped_itt].append((b,c))
                else:
                    mapped_ittdict[mapped_itt] = [(b,c)]
    G = GL(m, GF(2))
    ittset = set()
    ttlist = []
    for A in G.list():
        tt = [int(linear_mapf(boolf, A)(x)) for x in xrange(v)]
        itt = list_to_int(tt)
        if not itt in ittset:
            ittset.add(itt)
            ttlist.append(tt)
            if certify:
                if itt in mapped_ittdict:
                    print mapped_ittdict[itt], ':'
                    print A
                    sys.stdout.flush()
    return ttlist
