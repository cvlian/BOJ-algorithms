"""
    Binary Tree

    Note: 

    Type 1. 트리 순회_1991
"""

# Type 1. 트리 순회
def preOrder(p, adj, chk):

    chk[p] = 1
    print(chr(p+64), end='')

    if adj[p][0] != -1 and chk[adj[p][0]] == 0:
        preOrder(adj[p][0], adj, chk)

    if adj[p][1] != -1 and chk[adj[p][1]] == 0:
        preOrder(adj[p][1], adj, chk)

# Type 1. 트리 순회
def inOrder(p, adj, chk):

    chk[p] = 1

    if adj[p][0] != -1 and chk[adj[p][0]] == 0:
        inOrder(adj[p][0], adj, chk)

    print(chr(p+64), end='')

    if adj[p][1] != -1 and chk[adj[p][1]] == 0:
        inOrder(adj[p][1], adj, chk)

# Type 1. 트리 순회
def postOrder(p, adj, chk):

    chk[p] = 1

    if adj[p][0] != -1 and chk[adj[p][0]] == 0:
        postOrder(adj[p][0], adj, chk)

    if adj[p][1] != -1 and chk[adj[p][1]] == 0:
        postOrder(adj[p][1], adj, chk)

    print(chr(p+64), end='')