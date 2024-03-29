'''TRESC:
Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego
ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w
ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1'''
# there is a  bug wont fix it now 
from zad1ktesty import runtests
def roznica( S ):
    n = len(S) 
    T = [(0,0) for _ in range(n)]
    if S[0] == '0':
        T[0] = (1,0) 
    else:
        T[0] = (0,1)
    for i in range(1,n):
        if S[i] =='1':
            T[i] = (T[i-1][0],T[i-1][1]+1)
        else:
            T[i] = (T[i-1][0]+1,T[i-1][1]) 
    result = 0 
    for i in range(n):
        for j in range(n):
            roznica0 = T[i][0] - T[j][0] 
            roznica1 = T[i][1] - T[j][1] 
            if roznica0 - roznica1 > result:
                result = abs(roznica0 - roznica1) 
    return result

# Testy
runtests(roznica)
