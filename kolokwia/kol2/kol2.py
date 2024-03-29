#algorytm bledny i nie dziala 

from kol2testy import runtests
def findminmaxedge(G):
    #print("pokaz ",G)
    T1 = [] 
    n = len(G)
    for i in range(n):
        T1.append(G[i][0][1]) 
    #print("t1",T1)
    mini = max(T1)
    T1 = [] 
    for i in range(n):
        l = len(G[i])
        T1.append(G[i][l-1][1]) 
    maxi = min(T1)
    return mini,maxi
    
def graph_to_edge_list(G,n):
    L = [] 
    for i in range(n):
        for j,w in G[i]:
            if (j,i,w) not in L:
                L.append((i,j,w)) 
    return L

def kruskal(G,n,mini,maxi):
    s = list(range(n)) 
    m = len(G)
    r = [0 for _ in range(n)] 
    FLAG = True
    def find(u):
        if s[u]==u:
            return u 
        s[u] = find(s[u]) 
        return s[u] 
    def union(u,v):
        urep,vrep = find(u),find(v) 
        if urep != vrep: 
            if r[urep] > r[vrep]:
                s[vrep] = urep 
            elif r[vrep] > r[urep]:
                s[urep] = vrep 
            else:
                s[urep] = vrep 
                r[vrep] +=1 
    BEAUTREE = []
    
    G.sort(key = lambda a: a[2]) 
    if maxi < mini:
        maxi1,mini1 = mini,maxi
    else:
        maxi1,mini1 = maxi,mini
    for(u,v,t) in G:
        if t >=mini1 and t<=maxi1:
            if find(u) == find(v):
                #print('o',u,v,t)
                return False 
            else:
                union(u,v)
                #print('a: ',u,v,t)
                BEAUTREE.append((u,v,t)) 
    for i in range(1,n):
        if s[0] != s[i]:
            #print('b')
            FLAG = False
            break
    #print('g')
    if FLAG:
        print('c')
        return BEAUTREE
    for i in range(m):
        if G[i][2] == mini:
            indmin = i 
            break 
    for i in range(m-1,-1,-1):
        if G[i][2] == maxi: 
            indmax = i 
    for i in range(indmin-2,-1,-1):
        if find(G[i][0]) == find(G[i][1]):
            break 
        union(G[i][0],G[i][1])
        BEAUTREE.append((G[i][0],G[i][1],G[i][2]))
    FLAG = True 
    for i in range(1,n):
        if s[0] != s[i]:
            FLAG = False
            break
    if FLAG:
        #print("prosze")
        return BEAUTREE

    for i in range(indmax+1,m):
        if find(G[i][0]) == find(G[i][1]):
            break 
        union(G[i][0],G[i][1]) 
        BEAUTREE.append((G[i][0],G[i][1],G[i][2]))
    FLAG = True 
    for i in range(1,n):
        if s[0] != s[i]:
            FLAG = False
            break
    if FLAG:
        #print("return?")
        #print(BEAUTREE)
        return BEAUTREE
    return False 

            
       
def beautree(G):
    n = len(G) 
    for i in range(n): 
        G[i].sort(key = lambda a: a[1]) 
    mini,maxi = findminmaxedge(G)
    #print('mini,maxi: ',mini,maxi)
    L = graph_to_edge_list(G,n) 
    #print('krawedzie: ',L)
    T = kruskal(L,n,mini,maxi) 
    #print('co: ',T)
    if T == False:
        return None
    else:
        sum = 0
        n = len(T) 
        for i in range(n):
            sum += T[i][2] 

    return sum

#G = [[(1,2),(3,7)],
 #    [(0,2),(2,5)],
 #    [(1,5)],
 #    [(0,7)]]
#L = graph_to_edge_list(G,4)
#for i in range(4): 
        #G[i].sort(key = lambda a: a[1])
#mini,maxi = findminmaxedge(G)
#print(mini,maxi)
#print(L)
#print(kruskal(L,4,mini,maxi))
# zmien all_tests na True zeby uruchomic wszystkie testy
#G = [ [(1,3), (2,1), (4,2)], # 0
#[(0,3), (2,5) ], # 1
#[(1,5), (0,1), (3,6)], # 2
#[(2,6), (4,4) ], # 3
#[(3,4), (0,2) ] ] # 4
#print(beautree(G))
runtests( beautree, all_tests = True )
