def DFS_BRIDGES(G):
    n = len(G) 
    low = [-1 for _ in range(n)] 
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0 
    d = [-1 for _ in range(n)]
    bridges = []
    def DFSVisit(G,u):
        nonlocal time
        nonlocal bridges
        time +=1 #czas odwiedzenia
        low[u] = time
        d[u] = time 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]:
                parent[v] = u 
                DFSVisit(G,v)
            if low[v] < low[u] and parent[u] != v:
                low[u] = low[v] 
        if d[u] == low[u] and parent[u] != None: 
            bridges.append((parent[u],u))
        #time+=1 #czas przetworzenia
    for i in range(n):
        if not visited[i]:
            DFSVisit(G,i) 
    return bridges,low,parent 


G = [ [1,2], #0
     [0,2,3], #1
     [0,1,3,8], #2
     [1,2,4], #3
     [3,5,6], #4
     [4,6], #5
     [5,4,7], #6
     [6], #7
     [2,9,11], #8
     [8,10], #9
     [9,11], #10
     [8,10] #11
    ]

b,l,p =  DFS_BRIDGES(G) 
print(b)
print(l) 
print(p)



