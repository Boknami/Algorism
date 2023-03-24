import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    # 연관된 부분 다 끄집어 내서 비용 계산
    q = []
    disLeast = [1e9 for i in range(cnt_stu + 1)]# 최소 경로 비용 저장하는 배열

    heapq.heappush(q, (0, start)) # 큐에 시작 정보(시작지점이니 비용 0과 지점) 입력
    disLeast[start] = 0

    while(q):
        # 기록된 거리와 장소 끄집어내기
        dist, loc = heapq.heappop(q)

        for go,cost in graph[loc]:
            allCost = dist + cost
            if(allCost < disLeast[go]):
                disLeast[go] = allCost
                if(go == start) : continue
                heapq.heappush(q, (allCost, go))
    
    return disLeast

cnt_stu, cnt_road, placeParty = map(int,input().split())

graph = [[] for _ in range(cnt_stu+1) ]
for _ in range(cnt_road):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

lastValue = 0
for curLocation in range(1, cnt_stu+1):
    goCost = dijkstra(curLocation)
    backCost = dijkstra(placeParty)
    # 반환받은 최소 경로 비용 배열을 합산해 왕복 비용을 계산
    lastValue = max(lastValue, goCost[placeParty] + backCost[curLocation])
print(lastValue)