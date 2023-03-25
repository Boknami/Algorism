import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    costLeast = [ 1e9 for i in range(cntNode + 1)]# 최소비용 배열
    costLeast[start] = 0
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
    graph[end].append((start, cost))

mustGo1, mustGo2 = list(map(int,input().split()))
cost_start = dijkstra(1)
cost_mustgo1 = dijkstra(mustGo1)
cost_mustgo2 = dijkstra(mustGo2)
road1 = cost_start[mustGo1] + cost_mustgo1[mustGo2] + cost_mustgo2[cntNode]
road2 = cost_start[mustGo2] + cost_mustgo2[mustGo1] + cost_mustgo1[cntNode]

leastCost = min(road1, road2)
print(leastCost if leastCost < 1e9 else -1)