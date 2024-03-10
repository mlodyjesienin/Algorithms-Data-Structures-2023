from zad2testy import runtests

# FILIP ZIELINSKI
# algorytm o zlozonosci nlogn, opiera siê na tym, ¿e jezeli istnieje maksymalny
# wynik, to niezaleznie od drogi ktora do niego prowadzi, polega na zebraniu 
# pewnej ilosci z maksimow wszystkich elementow.
# algorytm nie daje odpowiedzi jaka jest ta droga, ktora nalezy wybrac, 
# a jedynie znajduje wyniki. 
# korzystam z quick sorta z dodatkowym warunkiem, ktory sprawia, ze sortowanie 
# drugiej czesci tablicy wykonuje sie tylko kiedy indeks jest mniejszy lub rowny
# wartosci, poniewaz tylko wtedy "druga" czesc tablicy nas jakkolwiek interesuje
# korzystam z mechanizmu, ze iteracje traktuje jako liczba dni i odejmuje
# stosowne wartosci. 

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
