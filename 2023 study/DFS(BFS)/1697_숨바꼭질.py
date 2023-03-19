from collections import deque

def bfs():
    q.append(cur)

    # 큐가 남아있는 동안 계속
    while(q):
        # 큐에 값 빼기
        now = q.popleft()

        # 원하던 값을 찾은 경우
        if(now == target):
            print(cnt[now])
            return
        
        # 원하던 값이 아니라면 => | -1칸 | +1칸 | *2칸 |
        for value in (now-1, now+1, now*2):
            # 이미 지나친 값은 넘기고 아닌 값은 횟수 증가하고 큐에 넣자
            if (0 <= value < MAX and cnt[value] == 0):
                cnt[value] = cnt[now] + 1
                q.append(value)

MAX = 100001 # 주어지는 값이 최대 10만

cur,target = map(int,input().split())
q = deque() 
cnt = [0] * MAX

bfs()
