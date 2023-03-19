import sys
from collections import deque
input=sys.stdin.readline

n,m = map(int,input().split())
graph = {}

for _ in range(m):
    Value, Key = map(int, input().split())

    # 딕셔너리 key가 존재하는지
    if Key in graph:
        graph[Key].append(Value)
    else:
        graph[Key] = [Value]

hacking = []
q = deque([])
max_v = 0
for i in graph:
    cnt = 0
    q.append(i)
    
    while(q):
        key = q.popleft()

        # Key가 딕셔너리에 존재한다면? (연결된 것이 있다면?)
        if(key in graph):
            q.extend(graph[key])
        cnt+=1
    hacking.append(cnt)

# 정렬을 하는데 어떻게 원래 위치를 기억할까..
# 최대 크기를 알아놓고 배열을 순회하면서 돌자!
max = max(hacking)

cnt = 0
for i in hacking:
    cnt +=1
    if(i == max):
        print(cnt, end=' ')