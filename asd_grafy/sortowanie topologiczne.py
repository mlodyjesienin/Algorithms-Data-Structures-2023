def reverse(T):
    n = len(T) 
    for i in range(n//2): 
        T[i], T[n-i-1] = T[n-i-1], T[i] 

def DAGsort(G): #Wariacja DFS, dodajemy do listy gdy przetworzymy 
    n = len(G) 
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0 
    T = [] 
    def DFSVisit(G,u):
        nonlocal time  
        time +=1 #czas odwiedzenia 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]:
                parent[v] = u 
                DFSVisit(G,v)
        T.append(v)
        time+=1 #czas przetworzenia
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i) 
    reverse(T)
    return T