import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q = deque()
    q.append([start,0])
    visited = [0] * 10000000 #방문여부체크 배열

    while(True):
        qq = q.popleft()
        q_value = qq[0] #큐에서 뽑은 값
        q_cnt = qq[1] #큐에 횟수

        # 큐 뽑은 거 연산
        for select in (q_value-1, q_value+1, q_value*2):
            # 종료조건
            if(select == target):
                return q_cnt+1
            
            # 방문여부 확인 후 큐에 넣자
            if(select <= 1000000 and visited[select] == 0):
                visited[select] = 1

                if(select == q_value*2):
                    q.append([select,q_cnt])
                else:
                    q.append([select,q_cnt+1])
                
start, target = map(int, input().split())
print(bfs())
