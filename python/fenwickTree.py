"""
    Fenwick Tree
"""
import math

class fenwickTree:

    def __init__(self, n, op, initval=0):
        self.size = n
        self.op = op

        self.v = [initval]*self.size

    def cal(self, p):
        ret = 0

        while p > 0:
            ret = self.op(ret, self.v[p])
            p -= (p & -p)

        return ret

    def update(self, p, v):

        while p < self.size:
            self.v[p] += v
            p += (p & -p)