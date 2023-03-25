import sys
input = sys.stdin.readline

locHome = []
cntHome, cntRouter = map(int, input().split())
for i in range(cntHome):
    locHome.append(int(input()))
locHome.sort()

mindist = 1
maxdist = locHome[-1] -  locHome[0]
cntPossibleRouter = 1
hint = 0
res = 0
# 정렬된 loc 리스트에 첫 번째부터 시작해서 거리 체크
while(mindist <= maxdist):
    standard = (mindist + maxdist)//2
    cntPossibleRouter = 1
    curIdx = 0
    
    for idxRouter in range(1, cntHome):
        dist = locHome[idxRouter] - locHome[curIdx]
        
        if(dist >= standard): # 포함될 수 있는 거리
            # 기준을 locHome[0]에서 locHome[idxRouter]로 변경해야한다.
            cntPossibleRouter += 1
            curIdx = idxRouter
        else : continue

    # 목표 갯수에 비교해서 큰지 작은지에 따라서
    if(cntPossibleRouter < cntRouter): # 못 미친다면? => 거리 축소
        maxdist = standard-1
    elif(cntPossibleRouter >= cntRouter):     # 넘었다면 => 거리를 더 확장
        mindist = standard+1
        res = standard
print(res)