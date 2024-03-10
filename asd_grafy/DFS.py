def DFS(G):
    n = len(G) 
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0 
    def DFSVisit(G,u):
        nonlocal time 
        time +=1 #czas odwiedzenia 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]:
                parent[v] = u 
                DFSVisit(G,v)
        time+=1 #czas przetworzenia
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i) 
    return visited,parent


G = [[1],[2],[0,3,9],[4,6],[5],[3],[5],[9],[3,7],[10],[8,5]] 
v,p = DFS(G) 
print(v) 
print(p)