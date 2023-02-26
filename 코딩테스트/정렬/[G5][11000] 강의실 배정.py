# 다른 방법
# 트리처럼 서로 연결되어 있으면 세는 연결요소?
import heapq
import sys
input=sys.stdin.readline

n = int(input())
schedule = []
P_q= []

for i in range(n):
    s, e = map(int, input().split())
    schedule.append([s, e])

# 시작 시간 기준으로 정렬
schedule.sort()

# 우선순위 큐에 시작 시간이 젤 빠른 거 삽입
heapq.heappush(P_q, schedule[0][1])

# 스케쥴 돌면서 종료시간, 최소 시작 시간 비교
for i in range(1, n):
    if(schedule[i][0] < P_q[0]): # 최소 시작 시간이 현재 강의보다 늦게 끝나면?
        heapq.heappush(P_q, schedule[i][1])
    else:
        heapq.heappop(P_q)
        heapq.heappush(P_q,schedule[i][1])

print(len(P_q))