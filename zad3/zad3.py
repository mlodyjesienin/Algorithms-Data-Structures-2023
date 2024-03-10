# FILIP ZIELIÑSKI

#w pierwszej kolejnosci iteruje po kazdym slowie i sprawdzam czy jest
#leksykograficznie pierwsze  w porownaniu do swojego rewersu. jesli nie jest, 
#zamieniam je na swoj rewers. Nastepnie sortuje counting sortem po ilosci liter
#w wyrazie nastepnie zestawy slow o tej samej dlugosci sortuje radiax sortem.
#wystarczy teraz przeiterowac po tablicy i zwrocic maksymalny spojny podciag 
#tych samych wyrazow. 
#zlozonosc obliczeniow¹ ciezko mi oszacowaæ, wydaje mi sie jednak ze nie jest
#kwadratowa wiec stawiam na O(N + nlogn) ale zalezy od tego jak dziala radiax
#sort itd. 


from zad3testy import runtests

 +def partition(T,p,r):
    x = T[r][1]
    i = p-1
    for j in range(p,r):
        if T[j][1] <= x:
            i+=1
            T[i],T[j] = T[j],T[i] 
    T[i+1],T[r] = T[r], T[i+1] 
    return i+1

def altered_quicksort(T,p,r):
    while p<r:
        q = partition(T,p,r)
        if (q-1) - p < r-(q+1): 
            altered_quicksort(T,p,q-1)
            p = q+1
        else:
            altered_quicksort(T,q+1,r) 
            r = q-1

def rewers(s,n):
    return s[::-1]

def right_position(s):
    n = len(s)
    i = 0
    while i< n//2 and ord(s[i]) == ord(s[n-1-i]):
        i+=1 
    if ord(s[i]) < ord(s[n-1-i]):
        return s,n
    else:
        T = (rewers(s,n),n)
        return T


def radixsort_letter(T,i,j,k,n):
    letters = [0 for _ in range(ord('z')-ord('a')+1)]
    TMP = [(0,n) for _ in range(j-i+1)]

    for m in range(i,j+1):
        letters[ord(T[m][0][k]) - ord('a')] +=1 

    for m in range(1,len(letters)):
        letters[m]+=letters[m-1]

    for m in range(j,i-1,-1):
        TMP[letters[ord(T[m][0][k]) - ord('a')]-1] = T[m] 
        letters[ord(T[m][0][k])-ord('a')] -=1 

    for m in range(i,j+1):
        T[m] = TMP[m- i]


def radixsort(T,i,j,n):
    for k in range(n-1,-1,-1):
        radixsort_letter(T,i,j,k,n)

def search_maxi(T,i,j):
    maxi = 1
    curr = 1
    a = T[i][0]
    for n in range(i+1,j+1):
        if T[n][0] == a:
            curr+=1 
        else:
            if curr >maxi: 
                maxi = curr 
            curr = 1 
            a = T[n][0] 
    if curr > maxi:
        maxi = curr
    return maxi

def find_max_min(T,n):
    mini = float('inf')
    maxi = 0
    for i in range(n//21):
        a = T[i][1] 
        b = T[n-1-i][1]
        if a<b:
            if a < mini:
                mini = a 
            if b > maxi:
                maxi = b 
        else: 
            if b< mini:
                mini = b
            if a > maxi: 
                maxi = a 
    return mini,maxi

def altered_countingsort(T,n,mini,maxi):
   
    T2 = [0 for _ in range(maxi-mini +1)] 
    TMP = [(0,0) for _ in range(n)]
    for i in range(n):
        T2[T[i][1]-mini] +=1
    for i in range(1,len(T2)):
        T2[i] += T2[i-1]
    for i in range(n):
        TMP[T2[T[i][1] - mini] -1] = T[i] 
        T2[T[i][1]-mini] -=1 
    for i in range(n):
        T[i] = TMP[i]

    
def strong_string(T):
    n = len(T) 
    maxi = 0
    for i in range(n):
        T[i] = right_position(T[i])
    mini1,maxi1 = find_max_min(T,n)
    if( maxi1 - mini1 > 100*n):
        print("quick")
        altered_quicksort(T,0,n-1)
    else:
        altered_countingsort(T,n,mini1,maxi1)
    i = 0
    j = 1 
    while j<n:
        a = len(T[i][0]) 
        while j<n and len(T[j][0]) == a:
            j+=1
        if j>n:
            break
        j-=1
        if j - i +1 > maxi: 
            radixsort(T,i,j,a)
            potential_maxi = search_maxi(T,i,j,)
            if maxi < potential_maxi:
                maxi = potential_maxi 

        i=j+1
        j= i+1
       
    return maxi

runtests( strong_string, all_tests= True )
