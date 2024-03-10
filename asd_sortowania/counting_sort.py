def counting_sort(T,maxi,mini):
    n = len(T)
    B = [0]*n 
    C = [0]*(maxi-mini +1) 
    m  = maxi-mini+1
    for i in range(n):
        C[T[i]-mini] +=1 
    for i in range(1,m):
        C[i]+=C[i-1]
    for i in range(n):
        B[C[T[i]-mini]-1] = T[i] 
        C[T[i]-mini] -=1
    for i in range(n):
        T[i] = B[i] 


T = [3,6,1,8,13,8,54,22,11,13,19,3,3,3,1,13,54,19]
n = len(T) 
print(n)
maxi = 54
mini = 1
counting_sort(T,maxi,mini)
print(T) 
print(len(T))