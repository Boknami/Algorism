import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, target):
    q = []
    costLeast = [1e9 for i in range(cntNode + 1)]# 최소비용 배열
    costLeast[1] = 1
    # 큐에 (비용,시작)
    heapq.heappush(q, (start, 0))

    # 연결된 거 다 빼자
    while(q):
        startNode, cost= heapq.heappop(q)
        for targetNode, gocost in graph[startNode]:
            allCost = cost + gocost
            if(allCost < costLeast[targetNode]):
                costLeast[targetNode] = allCost
                heapq.heappush(q, (targetNode, allCost))
    return costLeast


cntNode, cntLine = map(int,input().split())
graph = [[] for _ in range(cntNode + 1) ]

for _ in range(cntLine):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

mustGo1, mustGo2 = list(map(int,input().split()))
print(dijkstra(1,mustGo1))
print(dijkstra(2,mustGo2))
print(dijkstra(3,mustGo2))


# 단순 최소 경로가 아니라 꼭 들려야한다..
# 다익스트라(출발, 꼭 방문1) -> 다익스트라(출발, 꼭 방문2) -> 최종노드
# 다익스트라(출발, 꼭 방문2) -> 다익스트라(출발, 꼭 방문1) -> 최종노드
