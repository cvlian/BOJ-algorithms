"""
    Bipartite Graph
"""

# grp: 1 = (1st group), -1 = (2nd group)
def draw(p, grp, c, adj):
    c[p] = grp; ret = 1

    for r in adj[p]:
        if c[r] == 0:
            ret &= draw(r, -grp, c, adj)
        elif c[r] == grp :
            return False

    return ret

def chk_bipartite(adj):
    n = len(adj)

    c = [0]*n; f = True

    for i in range(n):
        if c[i] == 0 :
            f &= draw(i, 1, c, adj)

    print("possible" if f else "impossible")
