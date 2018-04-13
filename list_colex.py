import sys

def subset_list(n, k):
    v = []
    v.append(0)

    for i in range(1, k + 1):
        v.append(i)

    v.append(n + 1)
    
    done = False

    while not done:
        print(v[1:-1])

        if v[1] < n - k + 1:
            j = 0

            while True:
                j += 1

                if(v[j + 1] > v[j] + 1):
                    break

            v[j] = v[j] + 1
            
            for i in range(1, j):
                v[i] = i

        else:
            done = True


n = int(sys.argv[1])
k = int(sys.argv[2])

subset_list(n, k)
