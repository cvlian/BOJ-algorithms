"""
    Longest Increasing Subsequence (LIS) - O(N^2)

    Note: 

    Type 1. 최장 증가 수열_11053/2550

    Type 2. 최장 감소 수열_11722

    Type 3. 바이토닉 수열_11054
"""

# Type 1. 최장 증가 수열
def lis(a):
    n = len(a)
    d = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)

# Type 2. 최장 감소 수열
def lds(a):
    n = len(a)
    d = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if a[j] > a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)

# Type 3. 바이토닉 수열
def bts(a):
    n = len(a)
    di = [1]*n; dd = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if a[j] < a[i] and di[j] + 1 > di[i]:
                di[i] = di[j] + 1

    for i in reversed(range(0, n)):
        for j in reversed(range(i+1, n)):
            if a[j] < a[i] and dd[j] + 1 > dd[i]:
                dd[i] = dd[j] + 1

    M = 0

    for i in range(n):
        M = max(M, di[i]+dd[i]-1)

    return M



