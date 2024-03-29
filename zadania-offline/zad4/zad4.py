# Filip Zielinskis
#Za pomoca dwukrotnego uzycia BFS (raz wierzcholkiem startowym jest s a raz t)
#znajduje odleglosc kazdego wierzcholka od wierzcholkow s i t.
#znajac rowniez dlugosc najkrotszej sciezki, tworze podgraf, ktory zawiera
#tylko krawedzie nalezace do ktorejs z najkrotszych sciezek.
#Teraz za pomoca algorytmu z wykladu, znaduje w podgrafie most, jezeli takowy 
#istnieje to usuniecie go sprawi ze w oryginalnym grafie najkrotsza sciezka
#sie wydluzy.
#UWAGA! moj podgraf teoretycznie jest niespojny poniewaz zostawiam w nim 
#niepotrzebne wierzcholki (nie polaczone z niczym) dla zachowania ciaglosci
#oznaczen (zeby numer wierzcholka w podgrafie zgadzal sie z numerem wierzcholka
#w oryginalnym grafie). Wyszukiwanie mostow, jest jednak tak napisane,
#ze ignoruje te wierzcholki, wiec w praktyce nie ma to znaczenia.
#wykonuje 2-krotnie BFS i raz DFS, zatem w reprezentacji listowej grafu
#otrzymuje 
#zlozonosc O(v+e)


from zad4testy import runtests


def BFS(G, s):
    n = len(G)
    q = []
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    visited[s] = True
    q.append(s)
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        m = len(G[u])
        for i in range(m):
            v = G[u][i]
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                q.append(v)

    return d, visited

def podgraf(G,d1,d2,n, x):
    short = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            if d1[i] + d2[G[i][j]] + 1 == x or d2[i] + d1[G[i][j]] + 1 == x:
                short[i].append(G[i][j])
    return short
def DFS(G):
    def DFS_visit(G, u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        nonlocal d
        nonlocal low
        nonlocal bridges
        nonlocal FLAG
        time += 1
        d[u] = time
        low[u] = time
        visited[u] = True
        for i in range(len(G[u])):
            v = G[u][i]
            if not visited[v]:
                parent[v] = u
                DFS_visit(G,v)
            elif parent[u] != v and low[v] < low[u]:
                low[u] = low[v]
            if not FLAG:
                return
        if parent[u] is not None and low[parent[u]] > low[u]:
            low[parent[u]] = low[u]
        if low[u]==d[u]:
            FLAG = False
            bridges.append((parent[u],u))
        #time += 1

    n = len(G)
    time = 0
    bridges = []
    FLAG = True
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    low = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i] and len(G[i]) != 0:
            DFS_visit(G, i)
    if not FLAG:
        return bridges[0]
    return None


def find_bridge(G):
    bridge = DFS(G)
    if bridge != None and bridge[0] == None:
        return None
    return bridge


def longer( G, s, t ):
    n = len(G)
    d1, visited1 = BFS(G, s)
    d2 = BFS(G, t)[0] 
    x = d1[t]  # dlugosc najkrotszej sciezki
    if not visited1[t]:
        #sciezka w ogole nie istnieje
        return None

    G2 = podgraf(G,d1,d2,n,x)
    
    
    return find_bridge(G2)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests=True )