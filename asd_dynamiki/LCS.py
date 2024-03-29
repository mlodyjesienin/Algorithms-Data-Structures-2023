def LCS(A,B):
    n = len(A)
    m = len(B) 
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]
     
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] +1 
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    for i in range(n+1):
        print(F[i])
    return F[n][m] 

A ='abcd'
B = 'gacfdx'
LCS(A,B)
    
