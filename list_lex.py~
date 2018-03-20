def list_lex(N, K):
    def list_lex_helper(n, k, min_val):
        if k == 1:
            for i in range(1, n + 1):
                yield str(i + min_val)
            
            raise StopIteration()

        else:
            for i in range(1, n - k + 2):
                for j in list_lex_helper(n - i, k - 1, min_val + i):
                    yield str(i + min_val) + str(j)

    for i in list_lex_helper(N, K, 0):
        print(i)

list_lex(5, 3)
