from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

for i in range(1, n+1):
    deque.append(i)

while len(deque) !=1 :
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])