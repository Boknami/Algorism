import sys
import heapq
input = sys.stdin.readline

def dikjstra(start):
    q = []
    costLeast = [1e9 for i in range(cntCity+1)]
    heapq.heappush(q, (0, start))
    costLeast[start] = 0

    while(q):
        cost,startNode = heapq.heappop(q)

        for targetNode, gocost in graph[startNode]:
            allCost = cost + gocost
            if(costLeast[targetNode] > allCost):
                costLeast[targetNode] = allCost
                heapq.heappush(q, (allCost, targetNode))
    return costLeast
cntCity, cntRoad, cntPacking = map(int, input().split())

graph = [ [] for i in range(cntCity+1)]
for _ in range(cntRoad):
    start,end,cost = map(int, input().split())
    graph[start].append((end,cost))
    graph[end].append((start, cost))

startCost = dikjstra(1)
print(startCost)
# 어짜피 도로 포장하면 0 => 최소 경로를 구하는 것이 의미가 있을까?..
# 아니면 다익스트라 구해놓고 제거를 해볼까?
# 아니면 1->4 로 이동할 수 있는 경로를 전부 구해놓고 그 중 가장 무거운 걸 제거 => 근데 가장 무거운 걸 제거해도 그대로 일지도?..
# min(다익스트라, 다익 기반 무거운 거 제거)