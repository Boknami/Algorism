import heapq
import sys
input=sys.stdin.readline

n = int(input())
xy= []
P_q = []

for i in range(n):
    s,e = map(int, input().split())
    xy.append([s,e])

xy.sort()
heapq.heappush(P_q, xy[0][1])
length = 0

start = xy[0][0]
end = 0
for i in range(0, n-1):
    if(P_q[0] >= xy[i+1][0]): # 우선순위 큐에 값보다 다음 좌표가 작거나 같으면 합쳐서 긋자.
        heapq.heappop(P_q)
        heapq.heappush(P_q, xy[i][1])

        if(i+1 == n-1):
            length += xy[i+1][1] - start
            break
    else:
        length += (heapq.heappop(P_q) - start)
        heapq.heappush(P_q, xy[i+1][1])

        if(i+1 == n-1):
            length += xy[i+1][1] - xy[i+1][0]
        start = xy[i+1][0]
print(length)