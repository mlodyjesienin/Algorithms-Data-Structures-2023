#if i remember correctly, it is not my code it is code from github.com/matipl01 

def binary_search(arr, val):
    left_idx = 0
    right_idx = len(arr) - 1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if val > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  

def lis(arr):
    if len(arr) < 2: return len(arr)
    
    n = len(arr)
    last = []
    
    for i in range(n):
        j = binary_search(last, arr[i])
        if j == len(last): last.append(arr[i])
        else: last[j] = arr[i]
    
    print(last)
    
    return len(last)
