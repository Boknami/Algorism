import sys
sys.setrecursionlimit(10000)

# 재귀 dfs / num번 노드
def dfs(num):
    visited[num] = True # 방문 표시
    for i in graph[num]: # 자식 노드 하나씩 돌면서
        if not visited[i]:
            dfs(i)
            
N, M = map(int, input().split())
graph = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

# 노드에 연결 정보 담아주기
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 탐색
for j in range(1, N + 1):
    if not visited[j]: #아직 방문 안한 경우 dfs 탐색
        dfs(j) # 해당 dfs를 빠져나왔다면 연결된 노드들은 다 탐색한 거임.
        cnt += 1

print(cnt)