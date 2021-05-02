"""
    Breadth First Search

    Note:

    # Type 1. 미로 찾기
"""

# Type 1. 미로 찾기 (상하좌우로만 이동할 수 있다고 하자)_2178
"""
    INPUT 
        └m : 2차원 지도 (0:벽, 1:이동가능한 지점)
        └h : 미로의 세로 길이
        └w : 미로의 가로 길이

    OUTPUT
        └d : (1, 1)에서 (h, w)까지 가장 빨리 갈 수 있는 최단거리, 경로 자체가 존재하지 않으면 -1
"""
def sol_maze1(m, h, w):
    chk = [x[:] for x in [[0] * w] * h]
    d = 0

    q = [(0,0)]
    chk[0][0] = 1

    while q:
        tq = []
        d += 1

        for i, j in q:

            if (i, j) == (h-1, w-1):
                return d
                
            for ny, nx in zip([i-1, i+1, i, i], [j, j, j-1, j+1]):
                if ny >= 0 and nx >= 0 and ny < h and nx < w and m[ny][nx] and not chk[ny][nx]:
                    tq += [(ny, nx)]
                    chk[ny][nx] = 1

        q = tq

    return -1

# 지도를 한 번만 쓰고 말거면 'chk'를 따로 두지 않고, 이미 갔던 길을 '벽'으로 바꿔주는 것도 방법이다.
def sol_maze1_v2(m, h, w):
    d = 0

    q = [(0,0)]
    m[0][0] = 0

    while q:
        tq = []
        d += 1

        for i, j in q:

            if (i, j) == (h-1, w-1):
                return d
                
            for ny, nx in zip([i-1, i+1, i, i], [j, j, j-1, j+1]):
                if ny >= 0 and nx >= 0 and ny < h and nx < w and m[ny][nx]:
                    tq += [(ny, nx)]
                    m[ny][nx] = 0

        q = tq

    return -1

# Type 1. 미로 찾기 (벽을 한 번 부술 수 있다!)_2206
# 큐에 현재 위치를 저장할 때, 벽을 부쉈는지 아닌지를 3번째 parameter로 제공한다.
def sol_maze2(m, h, w):
    chk = [[x[:] for x in [[0] * 2] * w] for _ in range(h)]
    d = 0

    q = [(0,0,1)]
    chk[0][0][1] = 1

    while q:
        tq = []
        d += 1

        for i, j, k in q:

            if (i, j) == (h-1, w-1):
                return d
                
            for ny, nx in zip([i-1, i+1, i, i], [j, j, j-1, j+1]):
                if ny >= 0 and nx >= 0 and ny < h and nx < w :
                    if not m[ny][nx] and not chk[ny][nx][k] :
                        tq += [(ny, nx, k)]
                        chk[ny][nx][k] = 1
                    elif m[ny][nx] and k == 1 and not chk[ny][nx][0]:
                        tq += [(ny, nx, 0)]
                        chk[ny][nx][0] = 1

        q = tq

    return -1

# Type 1. 미로 찾기 (여러 대상이 동시에 움직임)_5427
# '상근이'와 '불'이라는 오브젝트가 동시에 인접한 칸으로 이동하며, 불이 붙은 곳은 상근이가 지나갈 수 없다.
def sol_maze3(m, h, w):
    q = []

    # 항상 불이 먼저 이동한다고 문제에서 제시했기에 큐에는 불의 좌표부터 넣는다.
    for i in range(h):
        for j in range(w):
            if m[i][j] == '*':
                q += [(i, j, '*')]

    for i in range(h):
        for j in range(w):
            if m[i][j] == '@':
                q += [(i, j, '@')]

    d = 0

    while q:
        tq = []
        d += 1

        for i, j, k in q:

            # 상근이가 지도 가장자리에 도착한 경우
            if k == '@' and (i == 0 or j == 0 or i == h-1 or j == w-1):
                return d
                
            for ny, nx in zip([i-1, i+1, i, i], [j, j, j-1, j+1]):
                if ny >= 0 and nx >= 0 and ny < h and nx < w and m[ny][nx] == '.':
                    tq += [(ny, nx, k)]
                    m[ny][nx] = k

        q = tq

    return -1