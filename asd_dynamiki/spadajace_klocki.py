def klocki(T):

    n = len(T) 
    F = [1 for _ in range(n)] 
    F[0] = 1 
    for i in range(n):
        for j in range(i):
            if F[j] >= F[i] and T[j][0] <= T[i][0] and T[j][1] >= T[i][1]:
                F[i] = F[j] +1
    x = max(F) 
    return n- x

T = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]

print(klocki(T))


def binary_search(arr, val, fn):
    left_idx = 0
    right_idx = len(arr) - 1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if fn(val, arr[mid_idx]):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array


def longest_seq(arr, fn=lambda a, b: a > b):
    if len(arr) < 2: return len(arr)
    
    n = len(arr)
    top = []
    
    for i in range(n):
        j = binary_search(top, arr[i], fn)
        if j == len(top): top.append(arr[i])
        else: top[j] = arr[i]
    
    return top


def count_removed_bricks(A: 'array of bricks spans'):
    n = len(A)
    A = longest_seq(A, lambda curr, prev: curr[0] >= prev[0])
    print(A)
    A = longest_seq(A, lambda curr, prev: curr[1] <= prev[1])
    print(A)
    return n - len(A)