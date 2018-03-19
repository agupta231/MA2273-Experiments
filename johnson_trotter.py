def unrank(M, n):
    pi = [0] * (n + 1)

    P = M
    for j in reversed(range(1, n + 1)):
        R = P % j
        P = P // j

        k = -1
        Dir = 0 

        if P % 2:
            k = 0
            Dir = 1
        else:
            k = n + 1
            Dir = -1
        
        C = 0
        while C < R + 1:
            k += Dir
            if pi[k] == 0:
                C += 1
        
        pi[k] = j

    return pi[1:]

print(unrank(999999, 12))
