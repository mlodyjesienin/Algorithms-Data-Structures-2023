#algorytm, który otrzymuje na wejściu pewien
#ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
#mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
#ciąg składa się wyłącznie z liter a i b.
#Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
#powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). 

def radix_sort_letters(t,i):
    L =[0,0]
    n = len(t)
    B = [0]*n
    for j in range(n):
        L[ord(t[j][i])-ord("a")] +=1
    L[1]+=L[0]
    for j in range(n-1,-1,-1):
        B[L[ord(t[j][i])-ord("a")]-1] = t[j] 
        L[ord(t[j][i])-ord("a")]-=1 
    for j in range(n):
        t[j] = B[j]



def radix_sort(t,k):
    for i in range(k-1,-1,-1):
        radix_sort_letters(t,i)


def f(s,k):
    n = len(s) - k + 1
    t = []
    for i in range(n):
        s1 = s[i:i+k]
        t.append(s1) 
    print(t)
    radix_sort(t,k) 
    n = len(t) 
    maxi =1
    counter = 1
    ind_max = 0
    ind_curr = 0
    for i in range(1,n):
        if t[i] == t[ind_curr]:
            counter+=1
        else:
            print(i,counter)
            if counter >maxi:
                ind_max = ind_curr
                maxi = counter 
            counter = 1
            ind_curr = i
    if counter>maxi:
        ind_max = ind_curr 
        maxi = counter
    print(t)
    return(t[ind_max],maxi,ind_max)



s = "abbaaaabbbbbabbabbbbbb"
print(f(s,3))