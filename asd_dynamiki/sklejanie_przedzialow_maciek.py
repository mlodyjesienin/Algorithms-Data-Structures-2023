from zad1testy import runtests

def b_search(T,p,r,x):
    while p<=r:
        q = p + (r-p)//2

        if T[q] == x: return q 

        elif T[q]<x:
            p = q+1 

        else:
            r = q-1 

    return -1



def intuse( I, x, y ):
    n = len(I) 
    t = [[] for i in range(2*n)]

    for i in range(n):
        t[2*i] = I[i][0] 
        t[2*i+1] = I[i][1] 

    t.sort() 
    T = [t[0]]
    for i in range(1,2*n):
        if t[i-1]!=t[i]:
            T.append(t[i])  

    for i in range(n): 
        I[i] = (b_search(T,0,len(T)-1,I[i][0]),b_search(T,0,len(T)-1,I[i][1]))

    
    x = b_search(T,0,len(T)-1,x)
    y = b_search(T,0,len(T)-1,y) 
    
    if x<0 or y<0:
        return []


    dp = [[] for i in range(y+1)] 

    for i in range(x+1,y+1):
        for j in range(n):
            if I[j][0] == x and I[j][1] == i:
                dp[i].append(j) 

            if I[j][1] == i and I[j][0]>x and len(dp[I[j][0]])>0:
                dp[i]+=dp[I[j][0]] 
                dp[i].append(j)
                

    for i in dp[-1]:
        print(I[i])
    return dp[-1] 

runtests( intuse )

