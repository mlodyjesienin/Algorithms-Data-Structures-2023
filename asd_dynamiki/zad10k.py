from zad10ktesty import runtests
import math
def dywany ( N ):
    inf  = float('inf')
    i = 1
    T = []
    while i*i <= N:
        a = i*i
        T.append(a) 
        i+=1
    Parent = [None]*(N+1)
    A = [inf]*(N+1) 
    A[0] = 0 
    A[1] = 1 
    for i in range(1,N+1):
        for j in T:
            if i-j >= 0:
                A[i] = min(A[i],A[i-j] +1) 
    return [A[N]]



runtests( dywany )

