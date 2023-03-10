from collections import deque
import sys
input=sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
graph = []
day = 0
q = deque([])
M,N = map(int, input().split())

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
            q.append([i,j])

while q:
    cur = q.popleft()

    # 상하좌우 판단
    for i in range(4):
        x = cur[0] + dx[i]
        y = cur[1] + dy[i]

        # 크기 안에서 & 0인 값 & 큐에 없는 값
        if( (0<= x <= N-1 and 0<= y<= M-1) and graph[x][y] == 0):
            q.append([x,y])
            graph[x][y] = graph[cur[0]][cur[1]] + 1
            print(q)

for i in (graph):
    for j in i:
        if(day < j) : day = j
        if(j == 0):
            print(-1)
            exit(0)
print(day - 1)