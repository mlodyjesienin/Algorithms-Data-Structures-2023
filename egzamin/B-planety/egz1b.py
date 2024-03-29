# FILIP ZIELI�SKI 
# F[i][b] - minimalny koszt dotarcia na planete i posiadaj�c dok�adnie b paliwa.
# TELEPORT[i] - oszacowanie dotarcia na planet� i u�ywaj�c teleportu. uzupe�niana na
# bie��co. 
# najpierw wype�niamy F[0][b]. �eby dosta� si� na planete 0 z ilo�ci� paliwa b, trzeba
# zatankowa� dok�adnie b paliwa na planecie 0. 
# Wype�niamy r�wnocze�nie pierwsze oszacowanie skorzystania z teleportu.
# iterujemy po i,b. Je�eli b = 0 to mogli�my dosta� si�  z teleportu, lub doj�� z
# planety i-1 maj�c dok�adnie b+dystans(i-1,i) (b=0) paliwa, wybieramy lepsze z dw�ch. 
# skoro b=0 to mo�emy r�wnie� skorzysta� z teleportu. Patrzymy gdzie prowadzi teleport,
# z i-tej planety (np. prowadzi do j). Szacujemy koszt dostania si� na j planete
# z uzyciem teleportu. wcze�niej m�g� ju� istnie� teleport do planety j, stad konieczno��
# porownania oszacowa�. Je�eli nowe jest lepsze, to uaktualniamy TELEPORT[j]  
# W przypadku gdy b>0 albo dostali�my si� z planety i-1 maj�c na niej dok�adnie
# b + dystans(i-1,i) paliwa, albo mogli�my dosta� si� z mniejsz� ilo�cia paliwa na 
# planete i oraz zatankowa� dopiero na tej planecie. 
# Zauwa�my, �e wystarczy rozwa�y� koszt sytuacji, w kt�rej dostali�my si� na i-t� 
# planete posiadaj�c b-1 paliwa i zatankowali�my dok�adnie 1 paliwo. 
# Jest tak dlatego, �e F[i][b-1] ju� rozwa�ali�my sytuacje, gdy mieli�my b-2 paliwa
# i tankowali�my dok�adnie 1 paliwo. Je�eli wtedy to oszacowanie okaza�o si� najlepsze,
# oraz dla F[b][i] najlepsze jest zatankowanie 1 jednostki paliwa, to tak naprawde 
# odpowiada to zatankowaniu wi�cej ni� jednego paliwa, ale rozwa�amy to krok po kroku.
# Ko�cowy wynik to F[n-1][0]
# oczywi�cie dla ka�dego oszacowania trzeba sprawdzi�, czy nie wychodzimy poza tablice
# czyli czy b+ dystans(i,i-1) <= E. 
# Przechodzimy po ka�dej kom�rce, w ka�dej wykonuj�c sta�� niezale�n� od n i E liczbe
# operacji. zatem z�o�ono�� O(nE) !!!
from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D) 
    F = [[float('inf') for _ in range(E+1)] for _ in range(n)] 
    TELEPORT = [float('inf') for _ in range(n)] 
    for b in range(E+1):
        F[0][b] = C[0]*b 
    j,w = T[0] 
    if j!=0:
        TELEPORT[j] = w 
    for i in range(1,n):
        for b in range(E+1):
            distance = D[i]-D[i-1]
            if b==0:
                if b+ distance <= E:
                    F[i][b] = min(TELEPORT[i],F[i-1][b+ distance] )
                else: 
                    F[i][b] = TELEPORT[i] 
                j,w  = T[i] 
                if j!= w and TELEPORT[j] > F[i][b] + w: 
                    TELEPORT[j] = F[i][b] + w
            else: 
                if b+ distance <= E: 
                    F[i][b] = min(F[i-1][b+distance], F[i][b-1] + C[i])
                else:
                    F[i][b] = F[i][b-1] + C[i] 

    return F[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
