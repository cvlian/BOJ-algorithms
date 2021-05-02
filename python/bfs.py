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
def sol_maze(m, h, w):
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
                    tq += [[ny, nx]]
                    chk[ny][nx] = 1

        q = tq

    return -1