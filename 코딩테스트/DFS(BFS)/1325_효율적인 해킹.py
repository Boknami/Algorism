import sys
input=sys.stdin.readline

n,m = map(int,input().split())
graph = {}

for _ in range(m):
    A, B = map(int, input().split())
    if B in graph:
        graph[B].append(A)
    else:
        graph[B] = [A]

hacking = []
for i in graph:
    cnt = 0
    q = [i]
    
    while(q):
        key = q.pop()
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
    if(i == max): print(cnt, end=' ')