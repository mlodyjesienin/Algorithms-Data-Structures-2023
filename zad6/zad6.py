#FILIP ZIELIÑSKI 
# program by³ prób¹ samodzielnego napisania wspomnianego na wyk³adzie 
# algorytmu Hopcrofta-Karpa. Próba nie do koñca udana poniewa¿
# z niezrozumia³ych dla mnie przyczyn w pewnych przypadkach program 
# zwraca zly wynik
# z tego wzgledu ze nie dziala i prawdopodobnie nie realizuje algorytmu
# ktory mial realizowac, zlozonosci wole nie szacowaæ. 




from zad6testy import runtests
from queue import Queue

def graphed(G,n):
    maxi = 0
    curr = 0
    for i in range(n):
        curr = max(G[i]) 
        if curr > maxi:
            maxi = curr 
    m = maxi
    G2 = [[] for _ in range(n+m+1)]
    nowy = n+m+1 
    for i in range(n):
       for x in G[i]:
           G2[i].append(x+n)
           G2[x+n].append(i) 
    return G2, nowy 

def modify(s,v,parent,NEW,M):
    NEW[s] = False 
    NEW[v] = False 
    k = v    
    while parent[k] !=s:
        M[k][parent[k]] *=-1 
        M[parent[k]][k]*=-1
        k = parent[k] 
    M[k][parent[k]] *=-1 
    M[parent[k]][k] *=-1


def BFS_MODIFIED(G,s,n,NEW,M):
    Q = Queue()
    type = [0 for _ in range(n)] 
    type[s] = -1;
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)] 
    Q.put(s)
    visited[s] = True 
    while not Q.empty(): 
        u = Q.get() 
        t = type[u] 
        for v in G[u]:
            if not visited[v]: 
                m = M[u][v] 
                if t*m == -1:
                    type[v] = -1*type[u] 
                    parent[v] = u 
                    visited[v] = True
                    if NEW[v]: 
                        return s,v,parent
                    Q.put(v)
    return -1,-1 , -1


def binworker( U ): 
     counter = 0 
     dl = len(U)
     G,n = graphed(U,dl)
     n = len(G)
     NEW = [True for _ in range(n)] 
     M = [[1 for _ in range(n)] for _ in range(n)] 
     for i in range(n):
         if NEW[i]:
             s,v,parent = BFS_MODIFIED(G,i,n,NEW,M)
             if v == -1:
                 break 
             modify(s,v,parent,NEW,M) 
     for i in range(n):
        for j in range(n):
            if M[i][j] == -1:
                counter +=1;


     return counter//2


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
