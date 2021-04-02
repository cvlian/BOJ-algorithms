"""
    Floyd Warshall
"""

import sys

class Floyd:

    def __init__(self, n, init_val=987654321):
        self.n = n
        self.d = [x[:] for x in [[init_val] * (n+1)] * (n+1)]

        for i in range(1, n+1):
            self.d[i][i] = 0

    def connect(self, q, bi_direct=False) :
        for _ in range(q):
            a, b, c = map(int, sys.stdin.readline().split())

            self.d[a][b] = min(self.d[a][b], c)

            if bi_direct :
                self.d[b][a] = self.d[a][b]

    def cal(self) :
        for k in range(1, self.n+1):
            for i in range(1, self.n+1):
                for j in range(1, self.n+1):
                    self.d[i][j] = min(self.d[i][k]+self.d[k][j], self.d[i][j])
    