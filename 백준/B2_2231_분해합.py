# 분해합 = 각 자리수의 합
# N 숫자 => X + X의 각 자리 합
# X 중 가장 작은 X를 구해라
N = int(input())


for i in range(1,N+1):
        temp = i
        sum = 0

        while(temp / 10 > 0):
            sum = int(temp % 10) + sum
            temp = int(temp / 10)
        
        if(sum + i) == N:
            print(i)
            break
        
        if(i == N):
            print(0)
            break
        
# 반복문 돌 때 범위 신경쓰기
# (1, N+1)