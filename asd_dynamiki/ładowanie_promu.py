'''
Treść zadania
Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, 
które stoją w kolejce, żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, 
który wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut. 
Auta muszą wjeżdżąc w takiej kolejności, w jakiej są podane w tablicy A.'''

# F[i][w] - czy da się rozmieścić pierwsze i auta tak, żeby zostało w miejscu 
# na lewym pasie

def prom(L,W):
    L = 100*float(L)
    L = int(L)
    n = len(W) 
    F = [[0 for _ in range(L+1)] for _ in range(n)] 

    for i in range(n):
        W[i] = int(100*float(W[i]))
        
    SUM = [] 
    suma = 0

    for i in range(n):
        suma+=W[i] 
        SUM.append(suma)  

    for i in range(W[0],L+1):
        F[0][i] = 1 

    for i in range(1,n): 
        for j in range(W[i],L+1):
            a = 0
            if j + W[i]<= L:
                a = F[i-1][j-W[i]]+1 
            b = 0 
            if SUM[i] - j + W[i] <= L:
                b = F[i-1][j] 
            F[i][j] = max(a, b)
    for i in range(n-1,-1,-1):
        for j in range(L,-1,-1):
            if F[i][j] !=0:
                return i, SUM[i],n 

L = 18.24

cars = [3.16, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]

print(prom(L,cars))