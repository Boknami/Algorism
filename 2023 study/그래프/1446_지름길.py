n,d = map(int, input().split())

cur = 0
dis = 0

for i in range(n):
    if(cur == d):
        break

    start, end, leng = map(int, input().split())
    
    if(leng > end-start or end > d or start < cur):
        continue
    
    if(cur < start):
        dis += (start - cur)
        cur = start

    if(cur == start):
        cur = end
        dis += leng
    
print(cur, dis)
if(cur < d) : dis += d-cur
print(dis)

