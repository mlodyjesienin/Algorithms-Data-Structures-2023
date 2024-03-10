# FILIP ZIELIÑSKI 
# wiêksza z wartoœci UP[i][j], DOWN[i][j] to d³ugoœæ najd³u¿szej œcie¿ki
# wychodz¹cej z (0,0) i koñcz¹cej siê w (i,j). wartoœci UP i DOWN dla 
# pierwszej kolumny s¹ oczywiste.  Nastêpnie iteruje po kolumnach. 
# oprócz brzegowych pól, uzupe³niam tablicê DOWN jako najd³u¿sza œcie¿ka
# zak³adaj¹c ¿e na pole (i,j) wchodzê z PRAWEJ strony lub z DO£U - st¹d nazwa 
# DOWN. analogicznie tablicê UP uzupe³niam jako najd³u¿sza œcie¿ka zak³adaj¹c
# ¿e wchodzê tylko z prawej strony lub z GÓRY. Ostatecznie wynikiem jest 
# wiêksza wartoœæ z DOWN i UP dotycz¹ca pola (n-1,n-1).
# Ka¿demu polu przygl¹dam siê tak naprawdê 2 razy ( raz dla UP raz dla DOWN).
# zatem wykonuje 2*n^2 czyli z³o¿onoœæ O(n^2).  

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
