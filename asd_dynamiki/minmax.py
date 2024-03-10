def maxmin(T,k):
    inf = float('inf')
    n = len(T)
    SUM = [] 
    suma = 0

    def function(i,j):
        nonlocal F,SUM,n
        best = 0
        for s in range(i+1):
            a = F[i-s][j-1]
            b = SUM[i] - SUM[i-s]
            c = min(a,b)
            best = max(best, c)
        return best

    for i in range(n):
        suma+=T[i] 
        SUM.append(suma)
    F = [[0 for _ in range(k+1)] for _ in range(n)] 
    for i in range(n):
        F[i][0] = SUM[i]
    for i in range(n):
        for j in range(1,i+1):
            if j>k:
                break
            F[i][j] = function(i,j)

    
    for i in range(n):
        print(F[i])
    return F[i][k]

A = [5,2,7,1,6,3,8,4,2,7]
k = 2
print(maxmin(A,k))

A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
#    [   15   ]  [  19  ]  [   22   ]
k = 2 
print(maxmin(A,k))