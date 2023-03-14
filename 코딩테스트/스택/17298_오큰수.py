import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
dq = deque(map(int,input().split()))

save=[]
list_max = max(dq)

while(dq):
    cnt=1
    cur = dq.popleft()

    # cur보다 큰 수가 존재하는 경우 while에 들어가게..
    if(cur == list_max or len(dq)== 0):
        save.append(-1)
        continue

    while(True):
        comp = dq.popleft()
        if (cur < comp):
            dq.appendleft(comp)
            break
        cnt+=1
    for i in range(cnt):
        save.append(comp)

for i in save:
    print(i, end= ' ')