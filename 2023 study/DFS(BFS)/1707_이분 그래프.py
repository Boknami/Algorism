import sys
from collections import deque
input=sys.stdin.readline

N = int(input())

for i in range(N):
    node, line = map(int,input().split())
    graph = [[0] for i in range(1000) for i in range(1000)]
    q = deque()

    # 노드 연결정보
    for j in range(line):
        n, l = map(int,input().split())
        graph[n][l] = 1
        graph[l][n] = 1
        
    