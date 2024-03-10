# f(i,b) = maksymalna suma cen przedmiotow ze zbioru {0,...i} których ³¹czna
# waga nie przekracza b. 
# f(i,b) = max(f(i-1,b),f(i-1,b-W[i]) + P[i])
def knapsack(W,P,B,n):
    F = [[0 for _ in range(B+1)] for _ in range(n)] 
    for b in range(W[0],B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(1,n):
            if b-W[i] >=0:
                F[i][b] = max(F[i-1][b],F[i-1][b-W[i]] + P[i])
            else:
                F[i][b] = F[i-1][b]
    return F[B][n-1]