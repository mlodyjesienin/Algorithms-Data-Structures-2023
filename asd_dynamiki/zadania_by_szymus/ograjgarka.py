'''TRESC:
Dana jest talia N kart wyrażona poprzez tablicę A liczb naturalnych zawierającą wartości tych
kart. Można przyjąć, że talia posiada parzystą ilość kart. Karty zostały rozłożone na bardzo
szerokim stole w kolejności pojawiania się w tablicy. Dziekan poinformował Cię, że
podwyższy Ci ocenę z WDI o pół stopnia, jeżeli wygrasz z nim w pewną grę, polegającą na
braniu kart z jednego lub drugiego końca stołu na zmianę. Zakładając, że zaczynasz
rozgrywkę, musisz znaleźć jaką maksymalnie sumę wartości kart uda Ci się uzyskać.
Jednak, co ważne, musisz przyjąć, że dziekan jest osobą bardzo inteligentną i także będzie
grał w 100% na tyle optymalnie, na tyle to możliwe. Aby nie oddawać losu w ręce szczęścia
postanowiłeś, że napiszesz program, który zagwarantuje Ci wygraną (lub remis). Twój
algorytm powinien powiedzieć Ci, jaka jest maksymalna suma wartości kart, którą masz
szansę zdobyć grając z Garkiem'''

from zad5ktesty import runtests
def stany(A,T,i,j):
    a = min(T[i+2][j],T[i+1][j-1]) + A[i]
    b = min(T[i][j-2],T[i+1][j-1]) + A[j] 
    return max(a,b)


def garek ( A ):
    n = len(A) 
    T = [[0 for _ in range(n)] for _ in range(n)] 

    for i in range(n-1):
        T[i][i+1] = max(A[i],A[i+1]) 

    for j in range(3,n,2):
        for i in range(n):
            if i+j<n:
                T[i][i+j] = stany(A,T,i,i+j)
    return T[0][n-1]

runtests ( garek )