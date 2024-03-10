''' 1) zaimplementowac algorytm Dijkstry
2) najkrotsze sciezki z zadanego Ÿród³a w DAG
3) Odtworzenie najkrótszej œciezki (wazonej) z Ÿród³a s do t.
4) G = (V,E) krawedzie maja wagi ze zbioru 1,....E parami rozne 
mamy x,y z V i mamy znalezc sciezke z x do y o najmniejszej sumie wag o
przechodizmy tylko po malejacych wagach.
5) wymiana walut  k = n na n -z kursami walut znalezc z - walute
zeby pomnazac pieniadze. 
6) najlepszy korzen - Acykliczny, spojny, warzony, nieskierowany T. 
szujamy wierzcholkka dla ktorego najwieksza odleglosc od innego wierzcholka
jest najmniejsza
7) stacje benzynowe A - B kazdy wierzcholek ma cene paliwa, krawedzie maja 
dl. w kilometrach, w kazdym wierzcholku jest stacja. D - pojemnosc baku 
auto pali 1l/1km  Dojechac jak najtaniej. 
8) V,E  - graf polaczen miedzy miastam, wagi to odleglosci. Mamy dwoch kierowcow
alicja i bob, zmienaja sie co miasto (prowadza na zmiane). zadane miasta 
startowe i koncowe. Alicja ustala trase i kto prowadzi pierwszy, chce prowadzic
jak najkrocej. '''

#1 algorytm dijsktry 
from queue import PriorityQueue



def dijkstra(M,s):  # (O(E log E hehe) 
    n = len(M)
    inf = float('inf')
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue 
    q.put((0,s,-1))

   
    while not q.empty():
        distance,u,p = q.get()
        if d[u] ==inf:
            d[u] = distance
            parent[u] = p
            for v in range(n) and d[v]==inf:
                if M[u][v] >=0 amd d[v]==inf:
                    q.put((d[u]+M[u][v],v))
    return d, parent 

def dijkstra(M,s):  # (O(VlogV hehe)
    n = len(M)
    inf = float('inf')
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue 
    q.put((0,s,-1))

   
    while not q.empty():
        distance,u,p = q.get()[1] 
        for _ in range(n):
            u = #minimalny_index
            U = 0 
            distance = inf 
            for i in range(n):
                if not visited[i] and distance > d[i]:
                    u = i 
            d[u] = distance 
            visited

    return d, parent 


#zad 2 - najkrotsze sciezki w DAGu - sortujemy topologicznie, bez kolejki
# rozpatrujemy w kolejnosci topologicznej  :)
#zad 5 - wymiana walut, zamieniamy wagi na liczby przeciwne do logarytmow
# z ich wag i wyszukujemy cykle ujemne. 
#zad 8 - kopiujemy nasz graf, jeden  oryginalnymi wagami dla alicji
# drugi z wagami 0 dla boba. nastepnie przepinamy wierzcholki odpowiednio
# z grafu alicji do grafu boba i vice versa hehe 
# nastepnie szukamy najkrotszej sciezki...