# 종이가 같은 색으로 이루어졌는가? => 처음부터 끝까지 비교
# 같은 색으로 이루어지지 않았다면 4개의 색종이로 분할 반복
# => 해당 사각형을 4개의 사각형 배열로 분할!
# 같은 색으로 분할 완료 => 1로 이루어졌는지, 2로 이루어졌는지 확인

num = int(input())

ary = [[int(x) for x in input().split()] for y in range(num)]

print(ary)
dim = num
blue = 0
white = 0

# 전체 배열부터 시작
# 분해 시작했다면 그 안에서 끝내고? 나오는 편으로

for a in ary:
    for i in range(dim - 1):
        #전체 색이 동일하지 않음
        if(ary[a][i] != ary[a][i + 1]):
