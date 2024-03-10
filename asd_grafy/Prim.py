from queue import PriorityQueue
def Prim(G,s):
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
                Q.put((w,u,v)) 
    return parent 


G = [[(1,1),(5,8),(4,5)],
     [(0,1),(2,3)],
     [(1,3),(4,4),(3,6)],
     [(2,6),(4,2)],
     [(3,2),(5,7),(0,5),(2,4)],
     [(4,7),(0,8)]]
print(Prim(G,2))