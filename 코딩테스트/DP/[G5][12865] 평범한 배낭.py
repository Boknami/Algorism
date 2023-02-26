# 가장 중요한 건 가치
# [1]우선순위 큐 : 무게 고려하니 애매하다..
# [2]모든 경우의 수를 탐색
# -> 무게를 우선으로 일단 넣을 수 있는 경우를 다 탐색
# -> 그러고 우선순위 큐를 적용하면 어떨까?
# 6, 5, (3,4)
# 즉 3,4,5,6 을 조합해서 7이 안 넘게 하는 경우를 찾자.

import sys
input=sys.stdin.readline

n, k = map(int, input().split())
things = []
values = []

for i in range(n):
    w, v = map(int,input().split())
    things.append([w,v])

things.sort()

for i in range(n):
    cur_k = things[i][0]
    value = things[i][1]

    for j in range(i+1, n):
        if(cur_k + things[j][0] > k):
            break
        else :
            cur_k += things[j][0]
            value += things[j][1]
    values.append(value)

values.sort()
print(values[-1])