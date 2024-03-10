# FILIP ZIELI�SKI 
# wi�ksza z warto�ci UP[i][j], DOWN[i][j] to d�ugo�� najd�u�szej �cie�ki
# wychodz�cej z (0,0) i ko�cz�cej si� w (i,j). warto�ci UP i DOWN dla 
# pierwszej kolumny s� oczywiste.  Nast�pnie iteruje po kolumnach. 
# opr�cz brzegowych p�l, uzupe�niam tablic� DOWN jako najd�u�sza �cie�ka
# zak�adaj�c �e na pole (i,j) wchodz� z PRAWEJ strony lub z DO�U - st�d nazwa 
# DOWN. analogicznie tablic� UP uzupe�niam jako najd�u�sza �cie�ka zak�adaj�c
# �e wchodz� tylko z prawej strony lub z G�RY. Ostatecznie wynikiem jest 
# wi�ksza warto�� z DOWN i UP dotycz�ca pola (n-1,n-1).
# Ka�demu polu przygl�dam si� tak naprawd� 2 razy ( raz dla UP raz dla DOWN).
# zatem wykonuje 2*n^2 czyli z�o�ono�� O(n^2).  

from zad7testy import runtests
def maze( L ):
    n = len(L) 
    T = [[-1 for _ in range(n)] for _ in range(n) ] 
    for i in range(n):
        if L[i][0] == '#' :
            break 
        T[i][0] = i 
    for i in range(1,n):
        for j in range(n):
            if T[j][i-1] != -1 and L[j][i] != '#':
                if T[j][i] < T[j][i-1] +1:
                    T[j][i] = T[j][i-1] +1
                a =  T[j][i-1] +1
                counter = 0
                for k in range(j+1,n):
                    if L[k][i] == '#': 
                        break 
                    counter +=1
                    if T[k][i] < a +counter :
                        T[k][i] =  a + counter
                        
                counter = 0 
                for k in range(j-1,-1,-1):
                    if L[k][i] == '#':
                        break 
                    counter +=1 
                    if T[k][i] < a + counter :
                        T[k][i] = a + counter
         
    return T[n-1][n-1] 
                       
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
