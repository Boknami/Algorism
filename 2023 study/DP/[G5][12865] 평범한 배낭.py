import sys
input = sys.stdin.readline

# 모든 경우 : N 100일때 물건을 넣고 빼고 하는..총 2의 100승
# 불가능하니까 DP를 이용

n, k = map(int, input().split())
things = [[0,0]]
graph = [[0 for i in range(k+1)] for j in range(n+1)]

for _ in range(n):
    w,v = map(int, input().split())
    things.append([w,v])

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]

        # 그래프 채우자
        if(w > j): # 현재 한계 무게j보다 크면 못 들어가!
            graph[i][j] = graph[i-1][j]#이전 값
        else: # 들어갈 수 있다!
            graph[i][j] = max(graph[i-1][j], v + graph[i-1][j-w])

print(graph[n][k])