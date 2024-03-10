def kruskal(G)   
    maxedge = max(G, key=lambda x: max(x[0], x[1]))
    n = max(maxedge[0], maxedge[1]) + 1
    
    s = list(range(n))
    r = [0] * n

    def find(u):
        if s[u] == u:
            return u
        s[u] = find(s[u])
        return s[u]

    def union(u, v):
        ur, vr = find(u), find(v)
        if ur != vr:
            if r[ur] > r[vr]:
                s[vr] = ur
            elif r[vr] > r[ur]:
                s[ur] = vr
            else:
                s[vr] = ur
                r[ur] += 1

    G.sort(key=lambda a: a[2])

    MST = []
    for (u, v, t) in G:
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, t))
    return MST
