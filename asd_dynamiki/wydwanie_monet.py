'''
Treść
Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. 
Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T 
(algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8+5+1+1 zamiast 5+5+5).
'''
def coins(T,x):
    n = len(T) 
   # T.sort()
    F = [float('inf') for _ in range(x+1)]
    F[0] = 0 
    for i  in range(1,x+1):
        for j in range(n):
            if i - T[j] >=0:
                F[i] = min(F[i],F[i-T[j]]+1)
    return F 

T = [2, 5]
x = 19 
print(coins(T,x)) 