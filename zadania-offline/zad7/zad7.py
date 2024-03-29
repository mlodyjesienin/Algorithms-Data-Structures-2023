# FILIP ZIELIŃSKI 
# Większa z wartości UP[i][j], DOWN[i][j] to długość najdłuższej ścieżki
# wychodzącej z (0,0) i kończącej się w (i,j). Wartości UP i DOWN dla 
# pierwszej kolumny są oczywiste. Następnie iteruję po kolumnach. 
# Oprócz brzegowych pól, uzupełniam tablicę DOWN jako najdłuższą ścieżkę
# zakładając, że na pole (i,j) wchodzi się z PRAWEJ strony lub z DOŁU - stąd nazwa 
# DOWN. Analogicznie tablicę UP uzupełniam jako najdłuższą ścieżkę zakładając,
# że wchodzi się tylko z prawej strony lub z GÓRY. Ostatecznie wynikiem jest 
# większa wartość z DOWN i UP dotycząca pola (n-1,n-1).
# Każdemu polu przyglądam się tak naprawdę 2 razy (raz dla UP, raz dla DOWN),
# zatem wykonuję 2*n^2, czyli złożoność O(n^2).  

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
