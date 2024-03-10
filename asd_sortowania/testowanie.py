def permutationmatrix(T):
    n = len(T) 
    M = [[0 for _ in range(n)] for _ in range(n) ]
    for i in range(n):
        a = T[i] -1
        M[a][i]=1 
    return M 
def push_to_top(M,a,b): 
    for i in range(b,a,-1):
        M[i],M[i-1] = M[i-1],M[i]
def transpozycja(T,i):
    A = T.copy()
    a = A.index(i) 
    b = A.index(i+1) 
    A[a], A[b] = A[b], A[a]
    return A

T = [2,4,5,1,3]
print(T)
M = permutationmatrix(T) 
for i in range(1,5):
    A = transpozycja(T,i)
    print(A)
