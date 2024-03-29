# FILIP ZIELI�SKI
# Na pocz�tku przy u�yciu funkcji regraph modyfikuje wej�ciowy graf w nast�puj�cy spos�b:
# podwajam ilo�c wierzcho�k�w. ka�dy wierzcho�ek i ma swojego odpowiednika i +n. 
# znalezienie si� w grafie na dowolnym wierzcho�ku i>=n symbolizuje obrabowanie kt�rego�
# zamku. Z tego powodu, je�eli mi�dzy wierzcho�kami i,j w oryginalnym grafie wyst�puje 
# kraw�d� o wadze w, to w naszym nowym grafie istnieje ta sama kraw�d� o tej samej wadze
# oraz bli�niacza kraw�d� mi�dzy wierzcho�kami i+n, j +n o wadze 2*w +r.
# Dodatkowo dla ka�dej kraw�dzi i,j dodajemy kraw�d� symbolizuj�c�, napa�c na zamek
# w j-tym wierzcho�ku, czyli kraw�d� i, j+n (skierowan�) o wadze w - V[i], czyli o 
# wadze zysku napadu na zamek. w - V[i] mo�e by� mniejsze od 0.Teraz wystarczy 
# tylko u�y� algorytmu do znajdowania najkrotszych �cie�ek w grafie wa�onym i wynik to 
# albo dist[t] albo dist[t+n], zale�nie czy bardziej op�aca si� napa�� na jaki� zamek
# czy nie.
#  Jednak przez ujemne kraw�dzie nie da si� skorzysta� z algorytmu dijkstry.
# �eby to omin��, zauwa�my, �e wagi ujemne wyst�puj� tylko na kraw�dzi oznaczaj�cej
# napa�� na zamek w danym momencie, te krawedzie s� skierowane w jedn� strone. 
# z tego powodu, je�eli decydujemy napa�c si� na jaki� zamek to przechodzimy po takiej
# kraw�dzi dok�adnie raz, a je�li nie decydujemy si� to dok�adnie 0 razy. 
# Z tego powodu, mo�na znale�� maxi = maksymalna warto�� zysku napadu na jaki� zamek i 
# powi�kszy� warto�� ka�dej kraw�dzi oznaczaj�cej napa�� o t� warto��.
# W ten spos�b te kraw�dzie przestan� by� ujemne i mo�na stosowa� algorytm dijkstry,
# a �e na drodze z s do t+n przeszli�my dok�adnie jedn� tak� kraw�dzi� to wynik to
# min( d[t], d[t] - maxi) 
# UWAGA: warunki zadania pozwalaj� na powtarzanie kraw�dzi, jednak oczywistym spostrze�eniem
# jest fakt, �e przy wagach nieujemnych najkr�tsza "droga" to zawsze najkr�tsza 
# "�cie�ka". Powtarza� kraw�dzie mo�na tylko przy wagach ujemnych, my mamy tu doczynienia
# z wag� ujemn� tylko przy ew. napa�ci i ten przypadek nasz Dijkstra rozwa�a,
# poniewa� �cie�ka z i do j+n a nast�pnie z j+n do i+n (tak naprawde powt�rzenie krawedzi)
# jest rozpatrywana.
# Modyfukuje graf zwiekszaj�c V dwukrotnie i E 3 krotnie. Z�o�ono�c Dijkstry:
# O(3ElogV) <= O(V^2logV) WZORC�WKA! 


from egz1Atesty import runtests
from queue import PriorityQueue
def dijkstra_list(G,s):
    n = len(G) 
    inf = float('inf')
    Q = PriorityQueue() 
    parent = [None for _ in range(n)] 
    d = [inf for _ in range(n)] 
    d[s] = 0
    Q.put((0,s,None)) 
    while not Q.empty():
        dist, v, p = Q.get() 
        if d[v] == inf:
            parent[v] = p 
            d[v] = dist 
        for (u,w) in G[v]:
            if d[u] == inf:
                Q.put((d[v]+w,u,v)) 
    return d 

def regraph(G,V,r):
    n = len(G) 
    m = 2*n 
    maxi = - float('inf')
    for i in range(n):
        for u,w in G[i]:
            if maxi < V[u] - w:
                maxi = V[u] - w 
    G2 = [[] for i in range(2*n)] 
    for i in range(n):
        for u,w in G[i]:
            G2[i].append((u,w)) 
            G2[i].append((u+n,w-V[u] + maxi)) 
            G2[i+n].append((u+n,2*w +r)) 
    return G2, maxi 

def gold(G,V,s,t,r):
  n = len(G)
  const = len(G)
  G2,maxi = regraph(G,V,r) 
  dist = dijkstra_list(G2,s) 
  result = min(dist[t],dist[t+n] - maxi)  
  return result
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
