from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def funkcja(root):
    r = root
    MaxWeight = root.fundusze
    F = [[0 for _ in range(MaxWeight+1)]] 
    cost = root.koszt 
    price = root.wyborcy
    for i in range(cost,MaxWeight+1):
        F[0][i] = price 
    r = r.next
    i = 1

    while r != None: 
        cost = r.koszt 
        price = r.wyborcy 
        F.append([0 for _ in range(MaxWeight+1)])
        for j in range(0,MaxWeight+1): 
            if j-cost >=0:

                F[i][j] = max(F[i-1][j],F[i-1][j-cost] + price)
            else:
                F[i][j] = F[i-1][j] 
        i+=1
        r = r.next
    return F[i-1][MaxWeight]
  
def wybory(T):
    n = len(T) 
    result = 0
    for i in range(n):
        result += funkcja(T[i]) 

    return result

runtests(wybory, all_tests = True)