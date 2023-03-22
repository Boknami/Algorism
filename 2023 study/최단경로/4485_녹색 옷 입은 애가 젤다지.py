import sys
from collections import deque
input = sys.stdin.readline

def BFS(cave, minMove):
    queue = deque()
    queue.append((0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while(queue):
        cX,cY = queue.popleft()
        for idx in range(4):
            moveX = dx[idx] + cX
            moveY = dy[idx] + cY

            # 허용 범위 내
            if((0 <= moveX < cave_size) and (0 <= moveY < cave_size)):
                # 지금 값이 더 괜찮으면 넣고 다시 큐에 넣기
                if(minMove[moveX][moveY] > minMove[cX][cY] + cave[moveX][moveY]):
                    minMove[moveX][moveY] = minMove[cX][cY] + cave[moveX][moveY]
                    queue.append((moveX,moveY))

cnt = 1
endValue = 0
while(True):
    cave_size = int(input())
    if(cave_size == endValue):break
    cave = []
    for i in range(cave_size):
        cave.append(list(map(int, input().split())))
    minMove = [[int(1e9) for i in range(cave_size)] for j in range(cave_size)]
    minMove[0][0] = cave[0][0]
    BFS(cave, minMove)
    print(f'Problem {cnt}: {minMove[cave_size-1][cave_size-1]}')
    cnt+=1

#BFS로 풀어볼까? => 지나간 흔적 남기기가 조금 애매한데?
# 1 3
# 2 7
# -> 1 3 7이 먼저 되서 11되버리면 어쩔래?
# -> visited를 없애고 모든 칸에서 다 계산해볼까..

