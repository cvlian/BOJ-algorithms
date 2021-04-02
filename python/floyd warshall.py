"""
    Floyd Warshall O(V^3)
    
    Note: 모든 정점사이의 최단 거리를 구해야 할 때는 플로이드 와샬 알고리즘을 사용하자
    
    Type 1. 모든 정점 사이의 최단경로_11404
    
    Type 2. 최단경로에 속하는 정점을 구해야 할 때_11780
    
    Type 3. 각 요소들의 전후관계_1613
            각자의 키 순서가 몇 번째일까?_2458/10159
            
    Type 4. 모든 정점간의 최단거리가 주어졌을 때, 간선의 최소 갯수?_1507
            (K를 통해 우회한 거리 == I->J의 거리라면.. => I->J를 연결하는 도로가 필요없음 [Otherwise], 그런 K가 없다면.. => I->J를 연결하는 도로가 필요)
    
    Type 5. 제일 길이가 짧은 사이클_1956
            (dist[i][i]를 초기화 하지 않고 플로이드 계산!)
    
    
"""

import sys

INF = 987654321

class Floyd:

    def __init__(self, n):
        self.n = n
        self.d = [x[:] for x in [[INF] * (n+1)] * (n+1)]
        self.detour = [x[:] for x in [[-1] * (n+1)] * (n+1)]

        for i in range(1, n+1):
            self.d[i][i] = 0

    def connect(self, q, bi_direct=False) :
        for _ in range(q):
            a, b, c = map(int, sys.stdin.readline().split())

            self.d[a][b] = min(self.d[a][b], c)

            if bi_direct :
                self.d[b][a] = self.d[a][b]

    def run(self) :
        for k in range(1, self.n+1):
            for i in range(1, self.n+1):

                if self.d[i][k] == INF:
                    continue

                for j in range(1, self.n+1):

                    if self.d[k][j] == INF :
                        continue

                    if self.d[i][j] > self.d[i][k]+self.d[k][j]:
                        self.d[i][j] = self.d[i][k]+self.d[k][j]
                        self.detour[i][j] = k

    def get_path(self, i, j):

        path =[i]
        self.find_path(i, j, path)
        path.append(j)

        return path

    def find_path(self, s, e, path):
        if self.detour[s][e] != -1 :
            self.find_path(s, self.detour[s][e], path)
            path.add(self.detour[s][e])
            self.find_path(self.detour[s][e], e, path)
    	
    
