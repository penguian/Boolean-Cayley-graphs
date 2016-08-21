def royle_x_graph():
    m = 8
    vecs = matrix(m,64)
    vecs[:,0] = vector([1]*8)
    k = 1
    for a in Combinations(xrange(1,m),4):
        vecs[:,k] = vector([-1 if x in a else 1 for x in xrange(m)])
        k += 1
    for b in Combinations(xrange(m),2):
        vecs[:,k] = vector([-1 if x in b else 1 for x in xrange(m)])
        k += 1
    A = matrix(64,64,0)
    for i in xrange(64):
        for j in xrange(i+1,64):
            if (vecs[:,i].T * vecs[:,j])[0,0] != 0:
                A[i,j] = 1
                A[j,i] = 1
    g = Graph(A)
    return g
