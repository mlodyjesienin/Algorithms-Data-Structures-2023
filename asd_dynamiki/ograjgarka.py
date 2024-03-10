from zad5ktesty import runtests
def stany(A,T,i,j):
    a = min(T[i+2][j],T[i+1][j-1]) + A[i]
    b = min(T[i][j-2],T[i+1][j-1]) + A[j] 
    return max(a,b)


def garek ( A ):
    n = len(A) 
    T = [[0 for _ in range(n)] for _ in range(n)] 

    for i in range(n-1):
        T[i][i+1] = max(A[i],A[i+1]) 

    for j in range(3,n,2):
        for i in range(n):
            if i+j<n:
                T[i][i+j] = stany(A,T,i,i+j)
    return T[0][n-1]

runtests ( garek )