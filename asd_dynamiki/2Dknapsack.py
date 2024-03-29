def knapsack2D(P,H,W,l,b):
    n = len(W) 
    F = [[[0 for _ in range(l+1)] for _ in range(b+1)] for _ in range(n)]
    for i in range(W[0],b+1):
        for j in range(H[0],l+1):
            F[0][i][j] = P[0] 

    for i in range(n):
        for j in range(b+1):
            for k in range(l+1):
                if j - W[i] >=0 and k-H[i] >=0:
                    F[i][j][k] = max(F[i-1][j][k],
                                    F[i-1][j-W[i]][k-H[i]] +P[i])
                else:
                    F[i][j][k] = F[i-1][j][k]

    for i in range(n):
        print('layer for item ',i,' = ') 
        for j in range(b):
            print(F[i][j])
       
    return F[n-1][b][l] 

P = [4, 10, 2, 3, 8]
W = [10, 6, 1, 2, 6]
H = [3, 9, 12, 4, 9]

MaxW = 12
MaxH = 20


print(knapsack2D(P, H, W, MaxH, MaxW))