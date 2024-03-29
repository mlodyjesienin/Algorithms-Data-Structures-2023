#Funkcja, ktora pozwala modyfikowac tablice i znajdywac za kazdym razem mediane w zlozonosci log(n)
def left(i):
    return 2*i +1 
def right(i):
    return 2*i +2 
def parent(i):
    return (i-1)//2 

def heapify_max(T,i,n):
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
        heapify_max(T,max_ind,n)

def heapify_min(T,i,n):
    r = right(i) 
    l = left(i) 
    min_ind = i 
    if l < n:
        if T[i] > T[l]:
            min_ind = l 
    if r <n:
        if T[min_ind] > T[r]: 
            min_ind = r
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind],  T[i] 
        heapify_min(T,min_ind,n)

 
def insert_min(T,a):
    T.append(a)
    n = len(T)
    new = n-1
    i = parent(new)
    while i >=0 and T[new] < T[i]:
        T[i], T[new] = T[new], T[i] 
        new = i 
        i = parent(i)
        
def insert_max(T,a):
    T.append(a)
    n = len(T) 
    new = n-1 
    i = parent(new)
    while i >= 0 and T[new] > T[i]: 
        T[i], T[new] =  T[new], T[i] 
        new = i 
        i = parent(i)

def median(T):
    n = len(T)
    Tmax = []
    Tmin = [] 
    maxi = T[0] 
    mini = -1
    lenmax = 1
    lenmin = 0 
    Tmax.append(T[0]) 
    for i in range(1,n):
        if T[i] < maxi:
            insert_max(Tmax,T[i])
            lenmax +=1
            if(lenmax - lenmin > 1):
                b = Tmax[0] # jak to sie zmieni z tym co jest wykomentowane to nie dziala
                Tmax[0] = Tmax[lenmax-1] 
                Tmax[lenmax-1] = b
                #Tmax[0],Tmax[lenmax-1] = Tmax[lenmax-1],T[0]
                print(Tmax)
                print(Tmax[lenmax-1])
                a = Tmax.pop()
                print(a)
                lenmax -=1 
                heapify_max(Tmax,0,lenmax) 
                insert_min(Tmin,a) 
                lenmin+=1
        else: 
            insert_min(Tmin,T[i])
            lenmin+=1 
            if(lenmin - lenmax > 0):
                b =  Tmin[0] 
                Tmin[0] = Tmin[lenmin-1]
                Tmin[lenmin-1] = b
                #Tmin[0], Tmin[lenmin-1] = Tmin[lenmin-1],Tmin[0] 
                a = Tmin.pop()
                lenmin -=1
                heapify_min(Tmin,0,lenmin)
                insert_max(Tmax,a) 
                lenmax+=1
        maxi = Tmax[0]
        print('MAX: ',end ='' )
        print(Tmax)
        print("MIN: ",end = '')
        print(Tmin)
    if n%2==1:
        return Tmax[0] 
    else:
        return ( Tmax[0] + Tmin[0] ) / 2

T = [1,12,3,4,8,9,10,5,2,6,7,11,13]
print(median(T))