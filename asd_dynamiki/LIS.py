def LIS(T): #n^2 
    n = len(T) 
    F = [1 for _ in range(n)] 
    for i in range(1,n):
        for j in range(0,i):
            if T[j] < T[i]:
                F[i] = max(F[i],F[j]+1) 
    return F[n-1]
            
