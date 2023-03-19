n, m = list(map(int,input().split()))
queue = list(range(1,n+1))
yose = []

cur = 0

while len(queue) > 1:
    cur = cur + m - 1

    while len(queue) <= cur:
        cur -= (len(queue))

    yose.append(queue.pop(cur))

yose.append(queue[0])
print("<" + ",".join(map(str,yose)) + ">" ,end="")