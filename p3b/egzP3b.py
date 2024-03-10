from egzP3btesty import runtests 
from queue import PriorityQueue



def Graph_to_list_of_edges(G,n):
    G2 = [] 
    SUM = 0
    for u in range(n):
        for v,w in G[u]:
            if u<v:
                SUM+=w
                G2.append((u,v,w)) 
    return G2,SUM

def kruskal(G,n):   
    n_edges = len(G) 

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

    G.sort(key=lambda a: -a[2])
    sum=0
    Flag = True
    for (u, v, t) in G:
        if find(u) != find(v):
            union(u, v)
            sum+=t 
        elif Flag: 
            sum+=t
            Flag=False
    return sum


def lufthansa ( G ):
    n = len(G) 
    G2,SUM = Graph_to_list_of_edges(G,n) 
    sum = kruskal(G2,n)
    return SUM - sum


runtests ( lufthansa, all_tests=True )