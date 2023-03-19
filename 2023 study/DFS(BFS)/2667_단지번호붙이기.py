visited = []
q = []
record = [] 

def search(a, b, idx):
    q.append([a,b]) # 접근한 인덱스 저장 [i][j] 
    record[idx] = record[idx] + 1 

    while(q):
        # 큐에서 빼내자
        cur = q.pop(0)

        # 1이면서 아직 방문 안했으면!
        if([cur[0],cur[1]] not in visited):
            #현재꺼 방문했다고 남기자
            visited.append([cur[0],cur[1]])
            
            # 연결 요소들 방문
            # (배열 범위 & 값 1 & 방문여부 & 큐에 있나 여부)

            #하측
            if(cur[0]+1 <= n-1 and graph[cur[0]+1][cur[1]] == 1 and [cur[0]+1,cur[1]] not in visited and [cur[0]+1,cur[1]] not in q):
                q.append([cur[0]+1,cur[1]])
                record[idx] = record[idx] + 1
            #상측
            if(cur[0]-1 >= 0 and graph[cur[0]-1][cur[1]] == 1 and [cur[0]-1,cur[1]] not in visited and [cur[0]-1,cur[1]] not in q):
                q.append([cur[0]-1,cur[1]])
                record[idx] = record[idx] + 1
            #우측
            if(cur[1]+1 <= n-1 and graph[cur[0]][cur[1]+1] == 1 and [cur[0],cur[1]+1] not in visited and [cur[0],cur[1]+1] not in q):
                q.append([cur[0],cur[1]+1])
                record[idx] = record[idx] + 1
            #좌측
            if(cur[1]-1 >= 0 and graph[cur[0]][cur[1]-1] == 1 and [cur[0],cur[1]-1] not in visited and [cur[0],cur[1]-1] not in q):
                q.append([cur[0],cur[1]-1])
                record[idx] = record[idx] + 1
    

n = int(input())
count = 0

# 2차원 배열 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        # 1이면서 방문체크가 안되있는 경우 실행
        if([i,j] not in visited and graph[i][j] == 1):
            record.append(0)
            search(i,j, count)
            count+=1 # 단지 갯수 파악

print(count) # 총 단지 개수
record.sort()
for i in record:
    if(i >= 1): print(i) # 각 단지 내 집의 수