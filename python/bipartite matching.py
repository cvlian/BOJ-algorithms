"""
    Bipartite Matching
"""

class biMatch:

    def __init__(self, n):
        self.nn = n
        self.adj = [[] for _ in range(n+1)]
        self.grpA = [0]*(n+1)
        self.grpB = [0]*(n+1)
        self.chk = []

    def connect(self, i, j):
        self.adj[i].append(j)

    def find(self, p):
        self.chk[p] = 1

        for q in self.adj[p]:
            if self.grpB[q] == 0 or (self.chk[self.grpB[q]] == 0 and self.find(self.grpB[q])):
                self.grpA[p] = q
                self.grpB[q] = p
                return True

        return False

    def sol(self):
        res = 0

        for i in range(1, self.nn+1):
            if self.grpA[i] == 0 :
                self.chk = [0]*(self.nn+1)
                if self.find(i):
                    res += 1

        return res