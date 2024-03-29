'''TRESC:
Pewien przedsiębiorca potrzebuje zamówić do swojej firmy dywany o łącznym polu
powierzchni wynoszącym N metrów kwadratowych. Nie martwi się on jakich będą one
wymiarów, ponieważ może je w dowolny sposób przycinać i łączyć. Aczkolwiek sklep, w
którym chce je kupić, sprzedaje tylko kwadratowe dywany o boku długości wyrażoną liczbą
naturalną określającą długość w metrach. Koszt zapakowania każdego dywanu jest stały
niezależnie od jego wielkości. Ze względów podatkowych przedsiębiorca potrzebuje
zminimalizować łączny koszt zapakowania dywanów, które zakupi, jednocześnie dbając o
środowisko nie może dopuścić, żeby jakikolwiek fragment dywanu się zmarnował. Twoim
zadaniem jako jego pracownika jest stworzenie listy wymiarów dywanów (wyrażonych jako
długość ich boku w metrach), które przedsiębiorca musi zakupić.'''

from zad10ktesty import runtests
import math
def dywany ( N ):
    inf  = float('inf')
    i = 1
    T = []
    while i*i <= N:
        a = i*i
        T.append(a) 
        i+=1
    Parent = [None]*(N+1)
    A = [inf]*(N+1) 
    A[0] = 0 
    A[1] = 1 
    for i in range(1,N+1):
        for j in T:
            if i-j >= 0:
                A[i] = min(A[i],A[i-j] +1) 
    return [A[N]]



runtests( dywany )

