"""
    미로 찾기

    Note: 

    Type 1. 오른쪽 아래 방향으로만 이동이 가능할 때_11048

    Type 2. 상하좌우로 이동이 가능할 때_1520
"""

# Type 1. 오른쪽 아래 방향으로만 이동이 가능할 때 (가능한 경로의 수 (1, 1) -> (h, w))
#         장애물의 경우 '-1'로 표시
def sol1(h, w, m, mod=100000007):
    d = [x[:] for x in [[0] * (w+1)] * (h+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if m[i][j] == -1 :
                continue

            d[i][j] = (d[i-1][j] + d[i][j-1])%mod

    return d[h][w]

# Type 1. 오른쪽 아래 방향으로만 이동이 가능할 때 (점수의 최대값)
def sol2(h, w, m):
    d = [x[:] for x in [[0] * (w+1)] * (h+1)]

    for i in range(1, h+1):
        for j in range(1, w+1):
            d[i][j] = m[i][j] + max(d[i-1][j], d[i][j-1])

    return d[h][w]

# Type 2. 상하좌우로 이동이 가능할 때 (1, 1) -> (h, w)
# 단, 상하좌우로 움직이는 데 조건 'f' 이 있음 (이동하는 방향에 제약이 없으면 사실상 경로의 수가 무한대...) 
def sol3(h, w, m, f=lambda x,y: x <= y):
    d = [x[:] for x in [[-1] * (w+1)] * (h+1)]

    def cal(y, x):

        if x == w and y == h :
            return 1

        if d[y][x] != -1 :
            return d[y][x]

        d[y][x] = 0

        for ny, nx in zip([y-1, y+1, y, y], [x, x, x-1, x+1]):

            if ny < 1 or nx < 1 or ny > h or nx > w :
                continue

            if f(m[y][x], m[ny][nx]):
                continue

            d[y][x] += cal(ny, nx)

        return d[y][x]

    return cal(1,1)