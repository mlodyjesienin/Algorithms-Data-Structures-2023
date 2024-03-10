from queue import Queue
def BFS(G,s):
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
        for v in G[u]:
            if not visited[v]:
                visited[v] = True 
                parent[v] = u 
                d[v] = d[u] +1 
                Q.put(v) 
    return visited,d,parent 


    

