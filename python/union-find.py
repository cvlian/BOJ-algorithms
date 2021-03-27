"""
    Union Find
"""

class UnionFind:

    def __init__(self, n):
        self.u = list(range(n+1))

    def find(self, p) :
        self.u[p] = self.find(self.u[p]) if self.u[p] != p else p
        return self.u[p]

    def merge(self, p, q) :
        p = self.find(p); q = self.find(q)
        self.u[q] = p
    
