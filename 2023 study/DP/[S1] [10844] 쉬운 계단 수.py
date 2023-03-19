import sys
input = sys.stdin.readline

n = int(input())

# 한 행에 10개를 담을 수 있고, n개의 열(자리수) 만들기
dp = [[0] * 10 for i in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        elif j >= 1 and j < 9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

all_num = int(sum(dp[n]) % 1000000000)
print(all_num)