from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    T = [0 for _ in range(n) ]
    maxr = 0
    teraz = 0
    P = -1
    radiusP = 0
    for i in range(n):
        r =1;
        if i - (P + radiusP) <0:
            if (2*P -i) - T[2*P-i] ==  P - radiusP:
                r = 2*P -i + 1
                while(s[i+r] == s[i-r] and i+r <n and i-r >-1):
                    r+=1
                T[i] = r-1
                if r > 1:
                    P = i 
                    radiusP = r-1 
            elif (2*P -i) - T[2*P-i] >  P - radiusP:
                T[i] = 2*P -i + 1
            else:
                T[i] = 2*P  - i + 1

        else: 
            while(s[i+r] == s[i-r] and i+r <n and i-r >-1):
                    r+=1
            T[i] = r-1
            if r>1:
                P = i 
                radiusP = r-1
        if r > maxr:
           maxr = r 
                
    return maxr 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
