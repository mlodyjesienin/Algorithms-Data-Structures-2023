import math
def bucketsort(T,n,maxi,mini):
    BUCKETS = [] 
    A = []
    for i in range(n):
        BUCKETS.append([]) 
    print(BUCKETS)
    p = (maxi-mini)/n
    print(p)
    for i in range(n):
        k = int((T[i]-mini)/p)
        BUCKETS[k].append(T[i]) 
    print(BUCKETS)
    for i in range(n):
        BUCKETS[i].sort()
    print(BUCKETS)
    for i in range(n):
        for j in range(len(BUCKETS[i])):
            A.append(BUCKETS[i][j])
    return A 
maxi = 189.1
mini = 154
n = 7
T = [154,176,158,189,165,162,170]
print(math.floor(0), math.ceil(0))
print(bucketsort(T,n,maxi,mini))