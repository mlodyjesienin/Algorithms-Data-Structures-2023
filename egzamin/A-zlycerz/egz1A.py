# FILIP ZIELIÑSKI
# Na pocz¹tku przy u¿yciu funkcji regraph modyfikuje wejœciowy graf w nastêpuj¹cy sposób:
# podwajam iloœc wierzcho³ków. ka¿dy wierzcho³ek i ma swojego odpowiednika i +n. 
# znalezienie siê w grafie na dowolnym wierzcho³ku i>=n symbolizuje obrabowanie któregoœ
# zamku. Z tego powodu, je¿eli miêdzy wierzcho³kami i,j w oryginalnym grafie wystêpuje 
# krawêdŸ o wadze w, to w naszym nowym grafie istnieje ta sama krawêdŸ o tej samej wadze
# oraz bliŸniacza krawêdŸ miêdzy wierzcho³kami i+n, j +n o wadze 2*w +r.
# Dodatkowo dla ka¿dej krawêdzi i,j dodajemy krawêdŸ symbolizuj¹c¹, napaœc na zamek
# w j-tym wierzcho³ku, czyli krawêdŸ i, j+n (skierowan¹) o wadze w - V[i], czyli o 
# wadze zysku napadu na zamek. w - V[i] mo¿e byæ mniejsze od 0.Teraz wystarczy 
# tylko u¿yæ algorytmu do znajdowania najkrotszych œcie¿ek w grafie wa¿onym i wynik to 
# albo dist[t] albo dist[t+n], zale¿nie czy bardziej op³aca siê napaœæ na jakiœ zamek
# czy nie.
#  Jednak przez ujemne krawêdzie nie da siê skorzystaæ z algorytmu dijkstry.
# ¯eby to omin¹æ, zauwa¿my, ¿e wagi ujemne wystêpuj¹ tylko na krawêdzi oznaczaj¹cej
# napaœæ na zamek w danym momencie, te krawedzie s¹ skierowane w jedn¹ strone. 
# z tego powodu, je¿eli decydujemy napaœc siê na jakiœ zamek to przechodzimy po takiej
# krawêdzi dok³adnie raz, a jeœli nie decydujemy siê to dok³adnie 0 razy. 
# Z tego powodu, mo¿na znaleŸæ maxi = maksymalna wartoœæ zysku napadu na jakiœ zamek i 
# powiêkszyæ wartoœæ ka¿dej krawêdzi oznaczaj¹cej napaœæ o t¹ wartoœæ.
# W ten sposób te krawêdzie przestan¹ byæ ujemne i mo¿na stosowaæ algorytm dijkstry,
# a ¿e na drodze z s do t+n przeszliœmy dok³adnie jedn¹ tak¹ krawêdzi¹ to wynik to
# min( d[t], d[t] - maxi) 
# UWAGA: warunki zadania pozwalaj¹ na powtarzanie krawêdzi, jednak oczywistym spostrze¿eniem
# jest fakt, ¿e przy wagach nieujemnych najkrótsza "droga" to zawsze najkrótsza 
# "œcie¿ka". Powtarzaæ krawêdzie mo¿na tylko przy wagach ujemnych, my mamy tu doczynienia
# z wag¹ ujemn¹ tylko przy ew. napaœci i ten przypadek nasz Dijkstra rozwa¿a,
# poniewa¿ œcie¿ka z i do j+n a nastêpnie z j+n do i+n (tak naprawde powtórzenie krawedzi)
# jest rozpatrywana.
# Modyfukuje graf zwiekszaj¹c V dwukrotnie i E 3 krotnie. Z³o¿onoœc Dijkstry:
# O(3ElogV) <= O(V^2logV) WZORCÓWKA! 


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
