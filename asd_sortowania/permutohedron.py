from queue import Queue
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
def BFS(G,s):
    n = len(G)
    visited = [False for _ in range(n)] 
    d = [-1 for _ in range(n)] 
    parent = [None for _ in range(n)] 
    d[s] = 0
    visited[s] = True
    Q = Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True 
                parent[v] = u 
                d[v] = d[u] +1 
                Q.put(v) 
    return d

def BFS2(G, s):
    n = len(G)
    q = []
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    visited[s] = True
    q.append(s)
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        m = len(G[u])
        for i in range(m):
            v = G[u][i]
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                q.append(v)

    return d

def transpozycja(T,i):
    A = T.copy()
    a = A.index(i) 
    b = A.index(i+1) 
    A[a], A[b] = A[b], A[a]
    return A

def CreateGraph(T):
    d = len(T) 
    G = [ [] for _ in range(d)] 
    n = len(T[0])
    for i in range(d):
        perm = T[i] 
        for j in range(1,n):
            neighbour = transpozycja(perm,j)
            G[i].append(T.index(neighbour))
    return G

def permutationmatrix(T):
    n = len(T) 
    M = [[0 for _ in range(n)] for _ in range(n) ]
    for i in range(n):
        a = int(T[i]) -1
        M[a][i]=1 
    return M 

def push_to_top(M,a,b): 
    for i in range(b,a,-1):
        M[i],M[i-1] = M[i-1],M[i]
       

def onestepcloser(M1,M2,a,counter):
    ind = M2.index(M1[a])
    if ind == a:
        return counter
    push_to_top(M2,a,ind)
    return counter+ind-a


def find_path(T,i,j,n):
    counter=0
    perm1 = T[i] 
    perm2 = T[j] 
    M1 = permutationmatrix(perm1) 
    M2 = permutationmatrix(perm2)
    for i in range(n-1):
        counter = onestepcloser(M1,M2,i,counter)
    return counter 
def list_of_str_to_int(T):
    n = len(T) 
    m = len(T[0]) 
    for i in range(n):
        for j in range(m):
            T[i][j] = int(T[i][j])

def compare():
    counter = 0
    data = list('12345')
    T = permutation(data)
    list_of_str_to_int(T)
    G = CreateGraph(T)
    n = len(T[0])
    m = len(G)
    print('m',m)
    print('n',n)
    for i in range(m):
        D = BFS(G,i)
        for j in range(i,m):
            distance = find_path(T,i,j,n)
            x = D[j]
            counter+=1
            if x != distance:
                print(T[i],T[j],distance, D)
                return False
            
    print(counter)
    return True

def classic(data,a,b):
    #data = list('12345')
    T = permutation(data)
    list_of_str_to_int(T)
    i = T.index(a) 
    j = T.index(b)
    G = CreateGraph(T)
    dl = BFS(G,i)[j] 
    return dl 

def moja(data,a,b):
    #data = list('12345')
    n = len(data)
    T = permutation(data)
    list_of_str_to_int(T)
    i = T.index(a) 
    j = T.index(b)
    dl = find_path(T,i,j,n)
    print(dl)
    return dl

def quickpath(perm1,perm2,n,counter):
    #print('counter',counter)
    if n==0:
        return counter
    ind =  perm1.index(1) 
    val = perm2[ind] 
    #print('v ',val,'perm1 ',perm1,'perm2 ', perm2)
    for i in range(n):
        perm1[i] -=1 
    perm11 = [] 
    for i in range(0,ind):
        perm11.append(perm1[i]) 
    for i in range(ind+1,n):
        perm11.append(perm1[i]) 
    ind2 = perm2.index(val) 
    for i in range(n):
        if perm2[i] > val:
            perm2[i] -=1 
    
    perm22 = []
    for i in range(0,ind2):
        perm22.append(perm2[i]) 
    for i in range(ind2+1,n):
        perm22.append(perm2[i]) 
    #print(perm11,perm22)
    return quickpath(perm11,perm22,n-1,counter+ val-1)


data = list('123456789') 
#perm1 = [3,2,8,6,4,7,1,5] 
#perm2 = [5,7,2,8,1,3,4,6]
#perm1 = [1,4,3,6,2,5] 
#perm2 = [3,2,6,4,5,1]
perm1 = [7,8,11,2,6,3,9,10,1,4,5] 
perm2 = [8,1,4,6,10,11,3,9,2,5,7]
n = len(perm1)
print('moj algorytm: ',quickpath(perm1,perm2,n,0))
perm1 = [2,4,7,1,3,5,6] 
perm2 = [6,3,2,5,4,7,1]
#moja(data,perm1,perm2)

#print('klasyczny algorytm: ',classic(data,perm1,perm2))
#print(compare())
