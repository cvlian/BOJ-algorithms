"""
    Change Making Problem

    Note: 

    Type 1. 각 동전을 사용하는 수에 제약이 없을 때_2293/2294/9084

    Type 2. 각 동전을 사용하는 수에 제약이 있을 때_2624/2091
"""

# Type 1. 각 동전을 사용하는 수에 제약이 없을 때 (경우의 수 구하기)
def coin1(a, MAX=100001):
    d = [1]+[0]*MAX

    for c in a:
        for i in range(0, MAX-c):
            d[i+c] += d[i]

    return d

# Type 1. 각 동전을 사용하는 수에 제약이 없을 때 ('k'원을 만들기 위해 필요한 동전의 최소 갯수)
def coin2(a, MAX=100001, INF = 987654321):
    d = [0]+[INF]*MAX

    for c in a:
        for i in range(0, MAX-c):
            d[i + c] = min(d[i]+1, d[i+c])

    return d

# Type 1. 각 동전을 사용하는 수에 제약이 없을 때 
# (각 동전이 다른 동전의 배수일 경우 e.g. 우리나라 화폐처럼 10, 50, 100, 500 ...)
def coin3(a, k):
    ret = 0
    a = sorted(a, reverse=True)

    for i in a:

        if k == 0 :
            break

        if k >= i:
            ret += k//i
            k %= i

    return ret

# Type 1. 각 동전을 사용하는 수에 제약이 없을 때 
# (각 동전이 다른 동전의 배수까지는 아니지만 주기성이 있을 때 e.g. 1398번 문제: 1, 10, 25, 100, 1000, 2500 ...)
# 동전 금액의 제일 앞의 2자리가 1, 10, 25 중 하나이므로, x < 100 인 x 에 대하여 sol(x) = sol(x * 10^2) = sol(x * 10^4) ...
def coin4(x, V, MOD=100):

    d = coin2(V, MAX=MOD)

    res = 0

    while x > 0 :
        res += d[x%MOD]
        x //= MOD

    return res

# Type 2. 각 동전을 사용하는 수에 제약이 있을 때 (경우의 수 구하기)
"""
    INPUT 
        └x : 만들고자 하는 액수
        └n : 동전의 가짓수
        └C : 각 동전의 갯수 
        └V : 각 동전의 금액

    OUTPUT
        └d[x] : x원을 만들 수 있는 경우의 수
"""
def coin5(x, n, C, V):
    dp = [1] + [0]*x

    for i, c, v in zip(range(n), C, V):
        for j in reversed(range(0, x)):
            if dp[j] != 0 :
                for k in range(1, c+1):

                    if j + v*k > x :
                        break

                    dp[j+v*k] += dp[j]

    return dp[x]

# Type 2. 각 동전을 사용하는 수에 제약이 있을 때 (동전을 최대한 많이 쓰기)
"""
    INPUT 
        └x : 만들고자 하는 액수
        └n : 동전의 가짓수
        └C : 각 동전의 갯수 
        └V : 각 동전의 금액

    OUTPUT
        └d[x] : x원을 만들기 위해 쓸 수 있는 최대 동전 갯수
        └res[x] : x원을 만드는 데 필요한 각 동전의 개수
"""
def coin6(x, n, C, V, INF = -987654321):
    dp = [0] + [INF]*(x+1)
    res = [[0]*4 for _ in range(x+1)]

    for i, c, v in zip(range(n), C, V):
        for j in reversed(range(0, x)):
            if dp[j] != INF :
                for k in range(1, c+1):

                    if j + v*k > x :
                        break

                    if dp[j+v*k] >= dp[j] + k :
                        continue

                    dp[j+v*k] = dp[j] + k
                    res[j+v*k] = [l for l in res[j]]
                    res[j+v*k][i] = k 

    return dp[x], res[x]