str = input()
res = 0

# 모든 경우의 수를 따져본다
for i in range(len(str)):
    if(str[i] == '-' ):
        # 다음에 num + num 이 존재하는 경우에는 묶고 계산 go
        for next in range(len(str)):
