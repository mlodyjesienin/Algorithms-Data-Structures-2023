def subsequence_equal_to_S(T,S):
    n = len(T) 
    T.sort() 
    F = [[False for _ in range(n)] for _ in range(S+1)]
    for i in range(n):
        F[0][i] = True 
    x = T[0] 
    for i in range(n):
        F[x][i] = True 
    for i in range(x+1,S+1):
        for j in range(1,n):
            if F[i][j-1]:
                F[i][j] = True 
                continue 
            a = i - T[j] 
            if a<0:
                continue 
            if F[a][j-1]:
                F[i][j] = True 
    return F[S][n-1] 

T = [7,3,2,5,13]
S = 19
print(subsequence_equal_to_S(T,S))