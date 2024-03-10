''' 1) insert/remove median (O(logn))
2) algorytm znajdowania k-tego najwiekszego el. w tablicy
3) algorytm sortujacy kwadraty naturalnych
4) sortowanie tablucy n elementowej ale logn roznych wartosci
5) sprawdz czy slowa A i B ¹ anagramami.
6) w tablicy A parami roznych liczb, znajdz x, y takie ze: x - y = max i nie ma
w tablicy liczb miedzy x i y '''



# 5)
# a)
def anagram(a,b):
    a_code = ord('a')
    z_code = ord('z')
    na = len(a)
    nb = len(b)
    if na!=nb:
        return False

    count_table_a = [0]*(z_code-a_code+1)
    count_table_b = [0]*(z_code-a_code+1)
    for i in range(na):
        count_table_a[ord(a[i])-a_code]+=1
        count_table_b[ord(b[i])-a_code]+=1
    return count_table_a == count_table_b
# b)
def anagram(a,b):
    import numpy
    c = numpy.empty(2**11)
    a_code = ord('a')
    z_code = ord('z')
    na = len(a)
    nb = len(b)
    if na!=nb:
        return False
    for i in range(na):
        c[ord(a[i])]=0
        c[ord(b[i])]=0
    for i in range(na):
        c[ord(a[i])]+=1
        c[ord(b[i])]-=1
    for i in range(na):
        if c[ord(a[i])]!=0:
            return False
    return True 
#3
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
            S[K[i]-1] = T[i]
            K[i] -=1
        return S
    T = sort2(T,0)
    T = sort2(T,1)
    for i in range(n):
        T[i] = n*T[i][1] + T[i][0]

print(sort([1,8,9,24,17]))