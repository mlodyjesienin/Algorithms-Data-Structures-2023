def partition(T,p,r,k):
    for i in range(p,r+1):
        if T[i] == k:
            m = i 
            break
    T[m], T[r] = T[r], T[m] 
    x = T[r] 
    i = p-1 
    for j in range(p,r):
        if T[j] <= x:
            i+=1
            T[i], T[j] = T[j], T[i] 
    T[i+1], T[r] = T[r], T[i+1]
    return i+1



def mediana_5(T,p,r):
        T2 = []
        if r - p +1 >=5:
            q = 5
        else:
            q = r-p
        for i in range(q):
            T2.append(T[p+i]) 
        T2.sort()
        if len(T2)==0:
            T2.append(T[p])
        return T2[q//2] 


def magiczne_piatki(T,p,r,k):
    if r<=p:
        return T[r]
    T_median = [] 
    for i in range(p,r+1,5):
        T_median.append(mediana_5(T,i,r))
    n = len(T_median)
    mediana_median = magiczne_piatki(T_median,0,n-1,n//2)
    q = partition(T,p,r,mediana_median) 
    if q==k:
        return T[q] 
    elif q >k:
        return magiczne_piatki(T,p,q-1,k) 
    else:
        return magiczne_piatki(T,q+1,r,k)

T = [10,5,8,1,2,6,9,0,3,4]
n = len(T)
k = 0
print(magiczne_piatki(T,0,n-1,k))
T2 = sorted(T) 
print(T2)
print(T2[k])


