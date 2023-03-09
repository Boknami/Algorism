graph = []
queue = []

M,N = map(int, input().split())

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
            queue.append([i,j])

day = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
temp_queue = []

# 큐를 2개 만들어서 하나는 소비용, 하나는 다음꺼 저장용
while(any(0 in l for l in graph)):
    day += 1
    while queue:
        cur = queue.pop()
        
        # 상하좌우 판단
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]

            # 크기 안에서 & 0인 값 & 큐에 없는 값
            if( (0<= x <= N-1 and 0<= y<= M-1) and graph[x][y] == 0 and [x,y] not in queue):
                temp_queue.append([x,y])
                graph[x][y] = 1

    queue = temp_queue[:]

print(graph, day)