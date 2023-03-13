import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
dq = list(map(int,input().split()))

# 스택을 이용
# 오른쪽에서부터 숫자를 꺼내는 아이디어
# 타 배열에 꺼낸 걸 저장
# 진행 : 반복 (끝보다 1칸 앞 ~ 0까지) 팝하고 appendleft()
# 현재 꺼낸 것과 배열에 첫 부분부터 검사

save_ary = [dq.pop()]
while(dq):
    cur = dq.pop()
    
    for i in save_ary:
        if(cur < i):
            print(cur)
            break
    dq.append(cur)