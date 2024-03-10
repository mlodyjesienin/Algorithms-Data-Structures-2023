def FloydWarshall(G):
    inf = float('inf') 
    M = G.copy() 
    n = len(M)
    P = G.copy 
    for t in range(n):
        for x in range(n):
            for y in range(n):
                a = M[x][y] 
                b = M[x][t] + M[t][y] 
                if a>b:
                    M[x][y] = b 
                    P[x][y] = P[t][y] 
    return M,P
