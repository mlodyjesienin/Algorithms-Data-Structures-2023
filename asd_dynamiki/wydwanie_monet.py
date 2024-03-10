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