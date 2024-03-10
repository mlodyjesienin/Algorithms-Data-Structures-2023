def map_cars(A, L):
    total = 0
    for i in range(len(A)):
        A[i] = int(A[i] * 100 + .5)
        total += A[i]
        # If we exceeded maximum possible length, return an index of the last car
        if total > 2 * L:
            return i - 1
    # If all may fit in, return the last possible car's index
    return len(A) - 1
    

def ferry(L: 'length of a ferry', A: 'array of cars lengths'):
    # Map all car lengths to the integer values (multiply by 100)
    # and leave all the cars which in no way can fit in the ferry
    n = len(A)
    L = int(100 * L + .5)
    last_i = map_cars(A, L)
    # Prepare array which will be used to cache values
    F = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(last_i + 1)]
    P = [''] * n
    
    def recur(i: 'current car index', 
              l: 'remaining space on the left lane',
              r: 'remaining space on the right lane'):
        # If the next car cannot fit in
        if l < 0 or r < 0:
            return False
        if i == 0:
            if l >= A[0]: P[0] = 'L'; return True
            if r >= A[0]: P[0] = 'R'; return True
            return False
        if F[i][l][r] is None:
            if recur(i - 1, l - A[i], r):
                F[i][l][r] = True
                P[i] = 'L'
            elif recur(i - 1, l, r - A[i]):
                F[i][l][r] = True
                P[i] = 'R'
        return F[i][l][r]
    
    for i in range(last_i, -1, -1):
        if recur(i, L, L):
            return i + 1, P
    return -1, []





#better 
def map_cars(A, L):
    total = 0
    for i in range(len(A)):
        A[i] = int(A[i] * 100 + .5)
        total += A[i]
        # If we exceeded maximum possible length, return an index of the last car
        if total > 2 * L:
            return i - 1
    # If all may fit in, return the last possible car's index
    return len(A) - 1
    

def ferry(L: 'length of a ferry', A: 'array of cars lengths'):
    # Map all car lengths to the integer values (multiply by 100)
    # and leave all the cars which in no way can fit in the ferry
    n = len(A)
    L = int(100 * L + .5)
    last_i = map_cars(A, L)
    # Prepare array which will be used to cache values
    F = [[None] * (L + 1) for _ in range(last_i + 1)]
    P = [''] * n
    # Calculate sums of all cars lengths from 'i'th index to the end
    S = [0] * (last_i + 2)
    S[last_i] = A[last_i]
    for i in range(last_i - 1, -1, -1):
        S[i] = S[i + 1] + A[i]
            
    # Index of the last car considered (which may fit into the ferry)
    end_idx = 0
    
    def remaining_right_space(i, l):
        all_sum = S[i + 1] - S[end_idx + 1]
        return L - (all_sum - (L - l))
    
    def recur(i: 'current car index', 
              l: 'remaining space on the left lane'):
        # If the next car cannot fit in
        r = remaining_right_space(i, l)
        if l < 0 or r < 0:
            return False
        if i == 0:
            if l >= A[0]: P[0] = 'L'; return True
            if r >= A[0]: P[0] = 'R'; return True
            return False
        elif F[i][l] is None:
            if recur(i - 1, l - A[i]):
                F[i][l] = True
                P[i] = 'L'
            elif recur(i - 1, l):
                F[i][l] = True
                P[i] = 'R'
        return F[i][l]
    
    for i in range(last_i, -1, -1):
        end_idx = i
        if recur(i, L):
            return i + 1, P
    return -1, []