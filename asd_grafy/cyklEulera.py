def Euler(G): # wariacja DFS, mozemy wchodzic do jedneog wierzcholka wiele razy
    n = len(G) 
    D = [0 for _ in range(n)] # tablica zapamietuje dla kazdego wierzcholka
                              # od jakiego elem. zaczac przegladac liste 
                              #sasiedztwa przy wchodzeniu kolejny raz do v.
    visited_edges = [[False for _ in range(n)] for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0 
    Cycle = []
    def DFSVisit(G,u):
        nonlocal time
        time +=1 #czas odwiedzenia 
        n = len(G[u])
        for i in  range (D[u],n): 
            v = G[u][i]
            if not visited_edges[v][u]:
                parent[v] = u 
                D[u] +=1
                visited_edges[v][u] = True 
                visited_edges[u][v] = True 
                DFSVisit(G,v)
        time+=1 #czas przetworzenia
        Cycle.append(u)
    #for i in range(n):
        #if not visited[i]:
    DFSVisit(G,0) 
    return Cycle 

G = [[1,2],[0,6,2,3,4,5],[0,1,6,3,5,4],[1,2,5,4],[3,1,2,5],[1,2,3,4],[1,2]]
#G = [[1,3],[0,2,3,4],[1,3],[0,1,2,4],[1,3]]
print(Euler(G))
