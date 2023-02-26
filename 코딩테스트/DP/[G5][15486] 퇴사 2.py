import sys
input=sys.stdin.readline

n = int(input())
schedual = []
profits = []

for i in range(n):
    t, p = map(int,input().split())
    schedual.append([t,p])

# 스케쥴 가능한 경우들 확인
for i in range(n):
    if(i + schedual[i][0] > n):
        continue
    profit = schedual[i][1]
    i = i + (schedual[i][0])

    for j in range(i, n):
        if(i + schedual[j][0] > n):
            continue
        else :
            i += schedual[j][0]
            profit += schedual[j][1]
    profits.append(profit)

profits.sort()
print(profits[-1])