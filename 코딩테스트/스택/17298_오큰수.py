import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
dq = deque(map(int,input().split()))

save=[]


while(dq):
    cnt=1
    list_max = max(dq)
    cur = dq.popleft()

    # 현재가 가장 큰 경우 or 더 이상 팝할게 없으면
    if(cur == list_max or len(dq) == 0):
        save.append(-1)
        continue
    
    # 반복 : 큐가 남아있는 동안
    while(dq):
        # 비교 값 pop
        comp = dq.popleft()

        # 현재 값보다 더 큰 값 존재
        if (cur < comp):
            dq.appendleft(comp) # 빼낸 거 다시 넣고
            break
            
        # 넘어간 비교숫자 갯수 기록
        cnt+=1
    
    # cnt만큼 배열에 기록한다.
    for i in range(cnt):
        save.append(comp)

for i in save:
    print(i, end= ' ')