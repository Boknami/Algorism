import sys
input = sys.stdin.readline

cntWood, needLength = map(int, input().split())
woods = list(map(int, input().split()))

# 이분탐색으로 길이를 '유추'하면서 맞춰보자
end = max(woods)
start = 0

# while로 원하는 숫자만큼 짜를 때까지 반복
while(start <= end):
    mid = (end + start)//2
    sum = 0

    # 나무들 중 현재mid보다 커서 1cm라도 짜를 수 있다면 짤라가보자
    for wood in woods:
        if(mid < wood):
            sum += wood-mid

    if(sum == needLength):
        print(mid)
        exit(0)
    elif(sum > needLength):
        start = mid + 1
    else:#더 필요하다
        end = mid - 1
print(end)