'''
Treść zadania
Zadanie 6 (ścieżka w drzewie)
Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma- potencjalnie ujemną wartość value(v). 
Proszę zaproponować algorytm, który znajduje wartość najbardziej wartościowej ścieżki w drzewie T.
'''



class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        self.f = -float('inf') 
        self.g = -float('inf')


def max_path(root):
    
    def g(v):
        if v.g != - float('inf'):
            return v.g 
        x = 0
        for vi in v.children:
            x = max(x,g(vi)) 
        x+= v.val 
        v.g = x 
        return v.g 

    def f(v):
        if v.f != -float('inf'):
            return v.f 
        if len(v.children) ==0:
            v.f = v.val
            return v.f 
        if len(v.children) ==1:
            v1 = v.children[0] 
            v.f = max(f(v1),f(v1)+v.val,v.val) 
            return v.f 
        a = -float('inf')
        for vi in v.children:
            a = max(a,f(vi),v.val) 
        x = g(v.children[0]) 
        y = g(v.children[1]) 
        best = max(x,y) 
        second = min(x,y)
        for vi in v.children:
            x = g(vi) 
            if best <= x: 
                second = best 
                best = x
        v.f = max(a,best + second + v.val) 
        return v.f

    return f(root)

