#일반적 소수 알고리즘 => 시간 초과
#에라토스테네스의 체 => 나누어 볼 숫자를 획기적으로 줄여준다.

#파이썬 => for안에 else를 통해 굳이 확인 변수를 심어둘 필요가 없다.
M, N = map(int, input().split())

for i in range(M, N+1):
    if(i == 1):
        continue

    for j in range(2, int(i** 0.5)+1):
        if i % j == 0:
            cut=1
            break
    else:
        print(i)