def BollmanFord(G,s):
    n = len(G) 
    inf = float('inf')
    d =[inf for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]
    for _ in range(n-1):
        for i in range(n): 
            for (j,w) in G[i]:
                if d[j] > d[i] + w:
                    d[j] = d[i] + w 
                    parent[j] = i  

    for i in range(n): 
        for (j,w) in G[i]:
            if d[j] > d[i] + w:
                return False 
    return d,parent 

