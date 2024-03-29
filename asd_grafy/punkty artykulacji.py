def ArticulationPoints(G):
    n = len(G) 
    visited = [ False for _ in range(n)] 
    parent = [None for _ in range(n)] 
    time = 0 
    low = [-1 for _ in range(n)] 
    d = [-1 for _ in range(n)] 
    art_points = []
    FLAG = [False for _ in range(n)]
    def DFSVisit(G,u):
        nonlocal time 
        time +=1 #czas odwiedzenia 
        low[u] = time 
        d[u] = time 
        visited[u] = True 
        for v in G[u]: 
            if not visited[v]:
                parent[v] = u 
                DFSVisit(G,v)
                if low[v] >= low[u] and u!=0: 
                    FLAG[u] = True
            if low[v] < low[u] and parent[u] != v:
                low[u] = low[v] 

        #time+=1 #czas przetworzenia
   
    DFSVisit(G,0) 
    counter = 0
    for v in G[0]:
        if parent[v] == 0:
            counter+=1
        if counter >=2: 
            art_points.append(0)
            break
    for i in range(n):
        if FLAG[i]:
            art_points.append(i)
    return art_points,parent


#G = [[1],[2],[0,3,9],[4,6],[5],[3],[5],[9],[3,7],[10],[8,5]] 
#v,p = DFS(G) 
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
print(ArticulationPoints(G)) 
