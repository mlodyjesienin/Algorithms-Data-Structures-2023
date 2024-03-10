from queue import PriorityQueue


def edge_to_list(G):
    maxedge = max(G, key=lambda x: max(x[0], x[1]))
    n = max(maxedge[0], maxedge[1]) + 1
    m = len(G) 
    G2 = [[] for _ in range(n)] 
    for i,j,w in G:
        G2[i].append((j,w)) 
        G2[j].append((i,w))
    return G2
def dijkstra_list(G,s):
    n = len(G) 
    inf = float('inf')
    Q = PriorityQueue() 
    parent = [None for _ in range(n)] 
    d = [inf for _ in range(n)] 
    d[s] = 0
    Q.put((0,s,None)) 
    while not Q.empty():
        dist, v, p = Q.get() 
        if d[v] == inf:
            parent[v] = p 
            d[v] = dist 
        for (u,w) in G[v]:
            if d[u] == inf:
                Q.put((d[v]+w,u,v)) 
    return d, parent



def kolokwium(G,s,t):
    n = len(G) 
    G2 = [[] for i in range(3*n)]
    for i in range(n):
        if i!=s and i!=t:
            for j,w in G[i]:
                if j!=s and j!=t:
                    G2[i].append((j+n,w)) 
                    G2[j+n].append((i+2*n,w)) 
    for i,w in G[s]:
        G2[s].append((i,w))
    for i,w in G[t]:
        G2[2*n+i].append((t,w))
    d = dijkstra_list(G2,s)[0] 
    print(d[t])
    #print(G2) 



G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
G2 = edge_to_list(G)
#print(G2)
kolokwium(G2,0,6)

