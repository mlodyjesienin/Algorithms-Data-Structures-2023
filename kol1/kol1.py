#FILIP ZIELINSKI
#Algorytm tworzy wszystkie potrzebne kolejne tablice p-elementowe (najpierw el. od 0 do p-1, pozniej od 1 do p itd)
#z kazdej z tablic wybierany jest k-ty najwiekszy element poprzez uzycie algorytmu magicznych piatek pokazanych na 
#wykladzie (partition, z dodatkowym poprawieniem wyboru pivota). prosze zwrocic uwage, ze k-ty najwiekszy el 
# w tablicy p-elementowej to ten, ktory po posortowaniu niemalejacym bedzie mial indeks p-k.
#magiczne pi¹tki dla tablicy p-elementowej dzialaja w O(p), a tych tablic bedzie troche mniej ni¿ n, st¹d
#zlozonosc to O(n*p)


from kol1testy import runtests




def partition(T,p,r,k):
    for i in range(p,r+1):
        if T[i] == k:
            m = i 
            break
    T[m], T[r] = T[r], T[m] 
    x = T[r] 
    i = p-1 
    for j in range(p,r):
        if T[j] <= x:
            i+=1
            T[i], T[j] = T[j], T[i] 
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def bubble_sort(T):
    n = len(T) 
    for i in range(n):
        for j in range(n-i-1):
            if T[j] > T[j+1]:
                T[j],T[j+1] = T[j+1], T[j] 

def mediana_5(T,p,r):
        T2 = []
        if r - p +1 >=5:
            q = 5
        else:
            q = r-p
        for i in range(q):
            T2.append(T[p+i]) 
        bubble_sort(T2)
        if len(T2)==0:
            T2.append(T[p])
        return T2[q//2] 


def magiczne_piatki(T,p,r,k): #algorytm zwraca 
    if r<=p:
        return T[r]
    T_median = [] 
    for i in range(p,r+1,5):
        T_median.append(mediana_5(T,i,r))
    n = len(T_median)
    mediana_median = magiczne_piatki(T_median,0,n-1,n//2)
    q = partition(T,p,r,mediana_median) 
    if q==k:
        return T[q] 
    elif q >k:
        return magiczne_piatki(T,p,q-1,k) 
    else:
        return magiczne_piatki(T,q+1,r,k)


def ksum(T, k, p):
    suma = 0
    n = len(T)
    for i in range(n-p+1):
        T2 = T[i:i+p]
        a =magiczne_piatki(T2,0,p-1,p-k)
        suma+=a 


    return suma




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
