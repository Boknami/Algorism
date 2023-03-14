import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
dq = deque(map(int,input().split()))

# 스택을 이용
# 오른쪽에서부터 숫자를 꺼내는 아이디어
# 타 배열에 꺼낸 걸 저장
# 진행 : 반복 (끝보다 1칸 앞 ~ 0까지) 팝하고 appendleft()
# 현재 꺼낸 것과 배열에 첫 부분부터 검사

save=[]
while(dq):
    cnt=1
    cur = dq.popleft()

    while(True):
        comp =dq.popleft()
        if (cur< comp):
            break
        cnt+=1
    for i in range(cnt):
        save.append(comp)
print(save)