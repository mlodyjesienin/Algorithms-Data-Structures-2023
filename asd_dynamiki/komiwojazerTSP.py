# F(i,j) =  koszt sciezek z 0 do i oraz z 0 do j ktore odwiedzaja wszystkie
# miasta od o do j ( j>i) i zadnego nie powtarzaja.
#f(0,1) = d(0,1)
# gdy i < j-1: f(i,j) = f(i,j-1) + d(j-1,j) - musimy sie dostac do j z j-1
# gdy i = j-1 f(j-1,j) = min po i<j-1 ( f(i,j-1) + d(i,j))
# O(n^2) zlozonosc
def TSP(A): 
    n = len(A) # A jest posortowane 
    D[i][j] = d(i,j) 
    F[i][j] = float('inf')
    def f(i,j):
        nonlocal F 
        nonlocal D 
        if F[i][j] != 0:
            return F[i][j] 
        if i < j-1:
            F[i][j] = f(i,j-1) + d[j-1][j] 
            return F[i][j] 
        #if i = j-1:  (tak naprawde)
        best = float('inf') 
        for k in range(j-1):
            best = min(best, f(k,j-1) + D[k][j]) 
        F[i][j] = best 
        return F[i][j]

