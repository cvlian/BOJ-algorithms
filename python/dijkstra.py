"""
    Dijkstra Algorithm
"""

from heapq import *

INF = 1234567890

class dijkstra:

    def __init__(self, n):
        self.hq = []
        self.adj = [[] for _ in range(n+1)]
        self.D = [INF]*(n+1)

    def update(self, u, v, w, bi_direct=True):
        self.adj[u].append((v, w))

        if bi_direct:
            self.adj[v].append((u, w))

    def sol(self, s):
        heappush(self.hq, (0, s))
        self.D[s] = 0

        while self.hq:
            d, p = heappop(self.hq)

            if d > self.D[p]:
                continue

            for np, w in self.adj[p]:
                if self.D[np] > self.D[p] + w :
                    self.D[np] = self.D[p] + w
                    heappush(self.hq, (self.D[np], np))


