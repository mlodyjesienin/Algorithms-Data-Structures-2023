#Funkcje sprawdzajace czy dwa slowa sa anagramami

# a)
def anagram(a,b):
    a_code = ord('a')
    z_code = ord('z')
    na = len(a)
    nb = len(b)
    if na!=nb:
        return False

    count_table_a = [0]*(z_code-a_code+1)
    count_table_b = [0]*(z_code-a_code+1)
    for i in range(na):
        count_table_a[ord(a[i])-a_code]+=1
        count_table_b[ord(b[i])-a_code]+=1
    return count_table_a == count_table_b
# b)
def anagram2(a,b):
    import numpy
    c = numpy.empty(2**11)
    a_code = ord('a')
    z_code = ord('z')
    na = len(a)
    nb = len(b)
    if na!=nb:
        return False
    for i in range(na):
        c[ord(a[i])]=0
        c[ord(b[i])]=0
    for i in range(na):
        c[ord(a[i])]+=1
        c[ord(b[i])]-=1
    for i in range(na):
        if c[ord(a[i])]!=0:
            return False
    return True 