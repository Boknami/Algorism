n,k = map(int, input().split())

up = 1
down = 1

# 5 * 4
cnt = n
for i in range(k):
    up = up * cnt
    cnt -= 1

for i in range(1, k+1):
    down *= i

print(int(up/down))