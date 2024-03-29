from queue import Queue
def BFSMATRIX(G,s):
    n = len(G)
    visited = [False for _ in range(n)] 
    d = [-1 for _ in range(n)] 
    parent = [None for _ in range(n)] 
    d[s] = 0
    visited[s] = True
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(n): 
            if M[u][i] = 0:
                conitnue 
            if not visited[i]:
                visited[i] = True 
                parent[i] = u 
                d[i] = d[u] +1 
                Q.put(i) 
    return visited,d,parent 

def find_path(G,s,t,parent):
    flow = float('inf')
    curr = t 
    T = []
    while parent[curr]!=s:
        T.append((p,curr))
        p = parent[curr]
        flow = mini(flow,G[p][curr]) 
        curr = p 
    T.append((s,curr)) 
    flow = mini(flow,G[s][curr])
    for u,v in T: 
        G[u][v] -= flow 
        G[v][u] += flow 
    return flow, G

def FORD_FULKERSON(G):
    n = len(G) 
    GR = G 
    max_flow=0 
    while True: 
        visited,d,parent = BFSMATRIX(GR,s) 
        if not visited[t]:
            return max_flow 
        curr_flow, GR = find_path(GR,s,t,parent) 
        max_flow+=curr_flow 




    

