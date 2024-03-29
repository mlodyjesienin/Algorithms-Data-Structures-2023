
def reverse_edges(G,n):
    G2 = [[] for _ in range(n)] 
    for i in range(n):
        for j in G[i]: 
            G2[j].append(i) 
    return G2

def DFS(G):
    RESULT =[] 
    n = len(G) 
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    T = [] 
    time = 0 
    Spojne = []
    def DFSVisit(G,u):
        nonlocal time 
        nonlocal visited 
        nonlocal parent 
        nonlocal T 
        time +=1 #czas odwiedzenia 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]:
                parent[v] = u 
                DFSVisit(G,v)
        T.append(u) 
        Spojne.append(u) 
        time+=1 #czas przetworzenia
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i)
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0
    Spojne = []
    G2 = reverse_edges(G,n)
    for k in range(n-1,-1,-1): 
        i = T[k] 
        if not visited[i]:
            DFSVisit(G2,i)
            RESULT.append(Spojne) 
            Spojne = []
    return RESULT


G = [[1],[2],[0,3,9],[4,6],[5],[3],[5],[9],[3,7],[10],[8,5]] 
print(DFS(G))