def left(i):
    return 2*i +1 
def right(i):
    return 2*i +2 
def parent(i):
    return (i-1)//2 
def heapify(T,i,n):
    r = right(i) 
    l = left(i) 
    max_ind = i 
    if l < n:
        if T[i] < T[l]:
            max_ind = l 
    if r <n:
        if T[max_ind] < T[r]: 
            max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind],  T[i] 
        heapify(T,max_ind,n)

def build_heap(T):
    n = len(T) 
    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n)  

def heapsort(T):
    n = len(T) 
    build_heap(T) 
    for i in range(n-1,0,-1):
        T[0], T[i] = T[i] , T[0] 
        heapify(T,0,i) 

#przykladowe wywolanie
T = [2,5,1,3,7,9,12,45,31,7]
heapsort(T)
print(T)