from zad1ktesty import runtests

def roznica( S ):
    n = len(S) 
    T = [(0,0) for _ in range(n)]
    if S[0] == '0':
        T[0] = (1,0) 
    else:
        T[0] = (0,1)
    for i in range(n):
        if S[i] =='1':
            T[i] = (T[i-1][0],T[i-1][1]+1)
        else:
            T[i] = (T[i-1][0]+1,T[i-1][1]) 
    result = 0 
    for i in range(n):
        for j in range(n):
            if i==0:
                roznica[]
            else:
                roznica0 = T[i-1][0] - T[j][1] 
            roznica2 = T[j][0] - T[j][1] 
            if abs(roznica2 - roznica1) > result:
                result = abs(roznica2 - roznica1) 
    return result

runtests ( roznica )