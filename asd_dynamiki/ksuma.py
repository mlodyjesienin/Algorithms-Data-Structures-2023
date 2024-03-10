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