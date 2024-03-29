from zad2testy import runtests

# FILIP ZIELIŃSKI
# Algorytm o złożoności nlogn opiera się na tym, że jeżeli istnieje maksymalny
# wynik, to niezależnie od drogi, która do niego prowadzi, polega on na zebraniu 
# pewnej ilości z maksimów wszystkich elementów.
# Algorytm nie daje odpowiedzi, jaka jest ta droga, która należy wybrać, 
# a jedynie znajduje wyniki. 
# Korzystam z quicksorta z dodatkowym warunkiem, który sprawia, że sortowanie 
# drugiej części tablicy wykonuje się tylko wtedy, gdy indeks jest mniejszy lub równy
# wartości, ponieważ tylko wtedy "druga" część tablicy nas jakkolwiek interesuje.
# Korzystam z mechanizmu, że iteracje traktuję jako liczbę dni i odejmuje
# odpowiednie wartości.


def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p,r):
        if T[j] >= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def prawie_quick_sort(T,p,r):
    if p < r:
        q = partition(T,p,r)
        prawie_quick_sort(T,p,q-1)
        if T[q] >= q:
            prawie_quick_sort(T,q+1,r)
    
def snow( S ):
    n = len(S)
    wynik = 0 
    prawie_quick_sort(S,0,n-1)
    iter=0;
    while(S[iter]>iter):
        wynik = wynik + S[iter] -iter 
        iter+=1
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
