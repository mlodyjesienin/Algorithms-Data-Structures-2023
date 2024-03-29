'''
Treść zadania
Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n x n. 
Szachownica zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów "w dół" oraz "w prawo". 
Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. 
Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
'''

def szachtraveleruwu(T):
    n = len(T)
    m = len(T[0])
    for i in range(1,m):
        T[0][i] = T[0][i-1] + T[0][i]
    for i in range(1,n):
        T[i][0] = T[i-1][0] + T[i][0] 
    for j in range(1,m):
        for i in range(1,n):
            T[i][j] = min(T[i-1][j], T[i][j-1]) + T[i][j] 
    return T[n-1][m-1] 

#T = [[3, 4, 5, 2, 1], [7, 2, 13, 7, 8], [3, 1, 4, 1, 5], 
#     [2, 8, 11, 1, 3], [3, 5, 1, 3, 2]]

T = [[1, 8, 11, 4, 2, 3, 2, 10, 18], [13, 11, 19, 19, 2, 11, 13, 16, 12], [19, 7, 2, 5, 14, 10, 14, 8, 8], [13, 1, 8, 11, 10, 16, 11, 12, 3], [6, 18, 5, 3, 1, 19, 15, 15, 19], [2, 19, 10, 16, 3, 9, 20, 12, 14], [1, 7, 12, 18, 5, 8, 1, 9, 9], [4, 18, 14, 1, 12, 12, 14, 14, 19], [3, 16, 7, 7, 19, 8, 8, 8, 18], [12, 20, 16, 17, 10, 12, 10, 13, 18], [7, 2, 14, 14, 4, 19, 7, 6, 12], [16, 4, 6, 17, 17, 7, 16, 15, 2], [14, 8, 12, 9, 6, 2, 3, 12, 4], [5, 18, 2, 15, 14, 2, 2, 16, 3]]
print(szachtraveleruwu(T))