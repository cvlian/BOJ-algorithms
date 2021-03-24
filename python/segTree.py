"""
    Segment Tree
"""

class segTree:

    def __init__(self, n, op, initval):
        self.size = 1
        self.op = op
        self.init_val = initval

        while n*2 > self.size: 
            self.size *= 2

        self.v = [self.init_val]*self.size

    def Fill(self, p):
        if p >= self.size//2:
            return self.v[p]
        
        self.v[p] = self.op(self.Fill(2*p), self.Fill(2*p+1))
        return self.v[p]

    def Cal(self, p, L, R, nodeL, nodeR):
        if R < nodeL or nodeR < L:
            return self.init_val
        if L <= nodeL and nodeR <= R:
            return self.v[p]

        m = (nodeL + nodeR)//2
        return self.op(self.Cal(2*p, L, R, nodeL, m), self.Cal(2*p + 1, L, R, m + 1, nodeR))

    def Update(self, p, v):
        p += self.size//2 - 1
        self.v[p] = v

        while p > 1:
            p //= 2
            self.v[p] = self.op(self.v[2*p], self.v[2*p + 1])