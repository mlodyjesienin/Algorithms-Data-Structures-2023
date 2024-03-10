def inwersje(T):
    suma = 0
   
    def mergesort(T):
        nonlocal suma
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
        nonlocal suma
        i=0
        j=0
        n = len(L)
        m = len(R)
        k = n
        A = []
        print(L,R)
        while(i<n and j<m):
            if L[i] <= R[j]:
                A.append(L[i]) 
                i+=1
                k-=1
            else:
                A.append(R[j])
                j+=1
                suma+=k
                print(suma,k)

        while i<n:
            A.append(L[i]) 
            i+=1
        while j<m:
            A.append(R[j]) 
            j+=1
        return A
    T2 = T.copy()
    mergesort(T2)
    return suma 

T = [5,1,2,3,4,2,2,5,1]
print(inwersje(T))
 
