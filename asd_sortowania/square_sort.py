# algorytm sortujacy kwadraty WSZYSTKICH liczb naturalnych od 1 do n
# najwyzszy nie moze byc kwadratem, musi byc o jeden mniejszy co najwyzej (nie bede tego naprawial po roku! )
def sort(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i]%n,T[i]//n)
    def sort2(T,x):
        n = len(T)
        K = [0 for _ in range(n)]
        for i in range(n):
            K[T[i][x]]+=1 
        for i in range(1,n):
            K[i] += K[i-1]
        S = [0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            S[K[T[i][x]]-1] = T[i]
            K[T[i][x]] -=1
        return S
    print("co", T)
    T = sort2(T,0)
    print("co2 ", T)
    T = sort2(T,1)
    for i in range(n):
        T[i] = n*T[i][1] + T[i][0]
    return T

print(sort([63,1,36,9,49,4,16,25]))