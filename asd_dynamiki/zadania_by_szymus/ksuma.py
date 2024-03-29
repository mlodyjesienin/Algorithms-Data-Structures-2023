'''TRESC:
Dla każdego ciągu n liczb możemy obliczyć k-ładną sumę (Zakładamy, że k <= n). Poprzez
k-ładną sumę rozumiemy minimalną sumę pewnych liczb wybranych w ten sposób, że z
każdych k kolejnych elementów wybraliśmy przynajmniej jeden z nich (w szczególności
oznacza to, że dla k=1 musimy wybrać wszystkie elementy, a dla k=n wystarczy wybrać
jeden, najmniejszy z nich). Proszę napisać algorytm, który dla zadanej tablicy liczb
naturalnych oraz wartości k oblicza k-ładną sumę.
'''

from zad3ktesty import runtests



def ksuma( T, k ): 
    n = len(T)
    
    for i in range(k,n):
        T2 = T[i-k:i] 
        mini = min(T2) 
        T[i]+= mini 
    T2 = T[n-k:n]
    mini = min(T2) 
    return mini

            
    
runtests ( ksuma )