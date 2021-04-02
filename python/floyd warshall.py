"""
    Floyd Warshall
"""

import sys

INF = 987654321

class Floyd:

    def __init__(self, n):
        self.n = n
        self.d = [x[:] for x in [[INF] * (n+1)] * (n+1)]
        self.detour = [x[:] for x in [[-1] * (n+1)] * (n+1)]

        for i in range(1, n+1):
            self.d[i][i] = 0

    def connect(self, q, bi_direct=False) :
        for _ in range(q):
            a, b, c = map(int, sys.stdin.readline().split())

            self.d[a][b] = min(self.d[a][b], c)

            if bi_direct :
                self.d[b][a] = self.d[a][b]

    def run(self) :
        for k in range(1, self.n+1):
            for i in range(1, self.n+1):

                if self.d[i][k] == INF:
                    continue

                for j in range(1, self.n+1):

                    if self.d[k][j] == INF :
                        continue

                    if self.d[i][j] > self.d[i][k]+self.d[k][j]:
                        self.d[i][j] = self.d[i][k]+self.d[k][j]
                        self.detour[i][j] = k

    def get_path(self, i, j):

        path =[i]
        self.find_path(i, j, path)
        path.append(j)

        return path

    def find_path(self, s, e, path):
        if self.detour[s][e] != -1 :
            self.find_path(s, self.detour[s][e], path)
            path.add(self.detour[s][e])
            self.find_path(self.detour[s][e], e, path)
    	
    