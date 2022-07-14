#혹시나 속도 에러 뜨면..
#import sys
#input=sys.stdin.readline

K = int(input())

document = []
extract = 0
sum = 0

#입력 받은 숫자만큼 반복 입력받기
for i in range(0, K):
    num = int(input())

    if(num == 0):
        extract = int(document.pop())
    else:
        document.append(num)

#배열 합 추출
for i in range(0, len(document)):
    sum = sum + document[i]

print(sum)