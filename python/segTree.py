"""
    Segment Tree
"""
import math

class segTree:

    def __init__(self, n, op, initval):
        self.size = 2**(math.ceil(math.log(n, 2)) + 1)
        self.op = op
        self.init_val = initval

        self.v = [self.init_val]*self.size

    def fill(self, p):
        if p >= self.size//2:
            return self.v[p]
        
        self.v[p] = self.op(self.fill(2*p), self.fill(2*p+1))
        return self.v[p]

    def cal(self, p, L, R, nodeL, nodeR):
        if R < nodeL or nodeR < L:
            return self.init_val
        if L <= nodeL and nodeR <= R:
            return self.v[p]

        m = (nodeL + nodeR)//2
        return self.op(self.cal(2*p, L, R, nodeL, m), self.cal(2*p + 1, L, R, m + 1, nodeR))

    def update(self, p, v):
        p += self.size//2 - 1
        self.v[p] = v

        while p > 1:
            p //= 2
            self.v[p] = self.op(self.v[2*p], self.v[2*p + 1])
