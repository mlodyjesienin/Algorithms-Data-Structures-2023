'''TRESC:
Dany jest ciąg macierzy A1,..,An. Ktoś chce policzyć iloczyn A1*A2*..*An. Macierze nie są koniecznie kwadratowe. 
Zależnie w jakiej kolejności wykonujemy mnożenia, koszt obliczeniowy może być różny. 
Należy podać algorytm znajdujący koszt mnożenia przy optymalbym doborze kolejności.
'''


def reverse(A):
    n = len(A)
    for i in range(n//2 +1):
        A[i],A[n-1-i] = A[n-1-i], A[i] 
    return A

def matrix_mulitplication_scarification(T):
    n = len(T) 
    x = T[0][0] 
    def cost(x,y,z):
        return x*y*z 
    F = [0 for _ in range(n)] 
    F[1] = cost(T[0][0],T[1][0],T[1][1])
    if n<3:
        return F[1]
    F[2] = min(F[1] + cost(x,T[2][0],T[2][1]),
             cost(T[1][0],T[1][1],T[2][1]) + cost(T[0][0],T[0][1],T[2][1]) )
    for i in range(3,n):
        F[i] = min(F[i-1] + cost(x,T[i][0],T[i][1]), 
                   F[i-2] + cost(T[i-1][0],T[i-1][1],T[i][1]))
    print(F)
    return F[n-1] 
A1 = [(1, 3), (3, 5)] # 15
A2 = [(1, 3), (3, 5), (5, 7)] # 50
A3 = [(40, 20), (20, 30), (30, 10), (10, 30)] # 26000 = (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
A4 = [(10, 20), (20, 30), (30, 40), (40, 30)] # 30K
A4 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1), (1, 9), (9, 6)] # 287
A5 = [(2, 2), (2, 8), (8, 6), (6, 9), (9, 9), (9, 2), (2, 1)] # 221


print(matrix_mulitplication_scarification(A5))
A6 = reverse(A5)  
print(matrix_mulitplication_scarification(A5))
print(A6)
