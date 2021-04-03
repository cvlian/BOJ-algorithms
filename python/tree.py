"""
    Tree

    Note: 
    
    Type 1. 트리의 지름 (임의의 두 정점 사이의 거리 중 가장 긴 것)_1167

    Type 2. 리프의 개수_1068

    Type 3. 그래프 내의 트리 개수_4803
"""

class Tree:

    def __init__(self, n, root = 1, bi_direct=True):
        self.nn = n
        self.root = root
        self.adj = [[] for _ in range(n+1)]
        self.diameter = -1
        self.bi_dir = bi_direct

    def connect(self, i, j, w=1):
        self.adj[i].append((j, w))

        if self.bi_dir :
            self.adj[j].append((i, w))

    # Type 1. 트리의 지름
    def cal_diameter(self):
        chk = [0]*(self.nn+1)
        self.lp = -1

        self.find_diameter(self.root, 0, chk)
        self.find_diameter(self.lp, 0, chk)

    # Type 1. 트리의 지름
    def find_diameter(self, p, w, chk):

        chk[p] = 1

        if self.diameter < w:
            self.diameter = w; self.lp = p

        for np, nw in self.adj[p]:
            if chk[np] == 0:
                self.find_diameter(np, w+nw, chk)

        chk[p] = 0

    # Type 2. 리프의 개수
    def cal_numOf_leaf(self):
        chk = [0]*(self.nn + 1)

        return self.find_leaf(self.root, chk)

    # Type 2. 리프의 개수
    def find_leaf(self, p, chk):

        chk[p] = 1

        res = 0

        if not self.bi_dir and len(self.adj[p]) == 0 :
            return 1

        if self.bi_dir and len(self.adj[p]) == 1 :
            return 1

        for np, nw in self.adj[p]:
            if chk[np] == 0:
                res += self.find_leaf(np, chk)

        return res


# Type 3. 그래프 내의 트리 개수
def chk_cycle(prev_p, curr_p, chk, adj):

    chk[curr_p] = 1

    for next_p in adj[curr_p]:

        if chk[next_p] == 1 and next_p != prev_p:
            return False

        if chk[next_p] == 0 and not chk_cycle(curr_p, next_p):
            return False

    return True

# Type 3. 그래프 내의 트리 개수
def find_trees(graph):
    res = 0

    chk = [0]*(graph.nn+1)

    for i in range(1, graph.nn+1):
        if chk[i] == 0 and chk_cycle(0, i, chk, graph.adj):
            res += 1

    return res


