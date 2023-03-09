from collections import deque

def bfs():
    q.append(cur)

    # 큐가 남아있는 동안 계속
    while(q):
        # 큐에 값 빼기
        now = q.popleft()
        if(now == target):
            print(cnt[now])
            return
        for value in (now-1, now+1, now*2):
            # 거치지 않았다면?
            if (0 <= value < 100001 and cnt[value] == 0):
                cnt[value] = cnt[now] + 1
                q.append(value)

cur,target = map(int,input().split())
q = deque()
cnt = [0] * 100001

bfs()
