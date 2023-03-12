import sys
from collections import deque
input=sys.stdin.readline

MAX = 1000001
def bfs():
    q = deque()
    q.append(start)
    visited = [0] * MAX #방문여부체크 배열
    visited[start] = 1

    while(True):
        q_value = q.popleft()

        if(q_value == target):
            print(visited[q_value] -1 )
            return
        
        # 큐 뽑은 거 연산
        for select in (q_value-1, q_value+1, q_value*2):
            # 방문여부 확인 후 큐에 넣자
            if(0 <= select <= MAX-1 and visited[select] == 0):
                if(select == q_value*2):
                    visited[select] = visited[q_value]
                    q.appendleft(select)
                else:
                    visited[select] = visited[q_value] + 1
                    q.append(select)


                
start, target = map(int, input().split())
bfs()