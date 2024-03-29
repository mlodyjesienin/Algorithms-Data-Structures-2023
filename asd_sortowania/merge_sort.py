def mergesort(T):
    n = len(T)
    if n>1:
        r = n//2;
        L = T[:r]
        R = T[r:]
        L =mergesort(L)
        R=mergesort(R)
        T =  merge(L,R)
    return T

def merge(L,R):
    i=0
    j=0
    n = len(L)
    m = len(R) 
    A = []
    while(i<n and j<m):
        if L[i] <= R[j]:
            A.append(L[i]) 
            i+=1
        else:
            A.append(R[j])
            j+=1

    while i<n:
        A.append(L[i]) 
        i+=1
    while j<m:
        A.append(R[j]) 
        j+=1
    return A

#przykladowe wywolanie
T = [1,3,7,2,13,4,11,6,-2,100,5,3,1,2,9] 
n = len(T)
print(n)
A = [2,4,5,8,9,11]
B = [4,13]
C = [2]
T=mergesort(T) 
n = len(T)
print(n)
print(T)
