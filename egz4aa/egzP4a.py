from egzP4atesty import runtests 

def binary_search(arr, val):
    left_idx = 0
    right_idx = len(arr) - 1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if val > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array

def LISn2(T): #n^2 
    n = len(T) 
    F = [1 for _ in range(n)] 
    for i in range(1,n):
        for j in range(0,i):
            if T[j] < T[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
    return max(F)
            

def lis(arr):
    if len(arr) < 2: return len(arr)
    
    n = len(arr)
    last = []
    
    for i in range(n):
        j = binary_search(last, arr[i])
        if j == len(last): last.append(arr[i])
        else: last[j] = arr[i]
    
    
    return len(last)
def mosty ( T ):
    T.sort(key=lambda a: (a[0],a[1]))  
    n = len(T) 
    T2 = [] 
    for i in range(n):
        T2.append(T[i][1]) 
    
    return LISn2(T2) 


runtests ( mosty, all_tests=True )