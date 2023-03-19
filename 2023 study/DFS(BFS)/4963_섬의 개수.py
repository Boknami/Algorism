row = 1
col = 1
map_inf = []

dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

def bfs(a, b):
    #현재꺼 큐에 넣고 상하좌우 대각에 있는 게 있다면 연결 ㄱ
    q = []
    q.append([a,b])

    while(q):
        cur = q.pop()
        for i in range(8):
            x = dx[i] + cur[0]
            y = dy[i] + cur[1]

            if(0 <= x <= col-1 and 0 <= y <= row-1 and map_inf[x][y] == 1):
                q.append([x,y])
                map_inf[x][y] += map_inf[cur[0]][cur[1]] + 1

while(row + col != 0):
    row,col = map(int,input().split())
    cnt = 0
    if(row + col == 0):break
    map_inf = []

    # 지도 정보 받기
    for i in range(col):
        map_inf.append(list(map(int,input().split())))

    # 이어져있는 섬을 파악하자.
    # 반복문으로 전체 돌고 1로 되어있다면 큐에 넣고 다음으로
    for k in range(col):
        for j in range(row):
            if(map_inf[k][j] == 1):
                bfs(k,j)
                cnt+=1
    print(cnt)