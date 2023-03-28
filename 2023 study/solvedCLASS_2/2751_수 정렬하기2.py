# 병합정렬을 이용해서 해결해볼 예정
n = int(input())
ary = []

for _ in range(n):
    ary.append(int(input()))

ary.sort()
for idx in ary:
    print(idx)