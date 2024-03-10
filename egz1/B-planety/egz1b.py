# FILIP ZIELIÑSKI 
# F[i][b] - minimalny koszt dotarcia na planete i posiadaj¹c dok³adnie b paliwa.
# TELEPORT[i] - oszacowanie dotarcia na planetê i u¿ywaj¹c teleportu. uzupe³niana na
# bie¿¹co. 
# najpierw wype³niamy F[0][b]. ¿eby dostaæ siê na planete 0 z iloœci¹ paliwa b, trzeba
# zatankowaæ dok³adnie b paliwa na planecie 0. 
# Wype³niamy równoczeœnie pierwsze oszacowanie skorzystania z teleportu.
# iterujemy po i,b. Je¿eli b = 0 to mogliœmy dostaæ siê  z teleportu, lub dojœæ z
# planety i-1 maj¹c dok³adnie b+dystans(i-1,i) (b=0) paliwa, wybieramy lepsze z dwóch. 
# skoro b=0 to mo¿emy równie¿ skorzystaæ z teleportu. Patrzymy gdzie prowadzi teleport,
# z i-tej planety (np. prowadzi do j). Szacujemy koszt dostania siê na j planete
# z uzyciem teleportu. wczeœniej móg³ ju¿ istnieæ teleport do planety j, stad koniecznoœæ
# porownania oszacowañ. Je¿eli nowe jest lepsze, to uaktualniamy TELEPORT[j]  
# W przypadku gdy b>0 albo dostaliœmy siê z planety i-1 maj¹c na niej dok³adnie
# b + dystans(i-1,i) paliwa, albo mogliœmy dostaæ siê z mniejsz¹ iloœcia paliwa na 
# planete i oraz zatankowaæ dopiero na tej planecie. 
# Zauwa¿my, ¿e wystarczy rozwa¿yæ koszt sytuacji, w której dostaliœmy siê na i-t¹ 
# planete posiadaj¹c b-1 paliwa i zatankowaliœmy dok³adnie 1 paliwo. 
# Jest tak dlatego, ¿e F[i][b-1] ju¿ rozwa¿aliœmy sytuacje, gdy mieliœmy b-2 paliwa
# i tankowaliœmy dok³adnie 1 paliwo. Je¿eli wtedy to oszacowanie okaza³o siê najlepsze,
# oraz dla F[b][i] najlepsze jest zatankowanie 1 jednostki paliwa, to tak naprawde 
# odpowiada to zatankowaniu wiêcej ni¿ jednego paliwa, ale rozwa¿amy to krok po kroku.
# Koñcowy wynik to F[n-1][0]
# oczywiœcie dla ka¿dego oszacowania trzeba sprawdziæ, czy nie wychodzimy poza tablice
# czyli czy b+ dystans(i,i-1) <= E. 
# Przechodzimy po ka¿dej komórce, w ka¿dej wykonuj¹c sta³¹ niezale¿n¹ od n i E liczbe
# operacji. zatem z³o¿onoœæ O(nE) !!!
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
