n = int(input())
ary = []

for _ in range(n):
    ary.append(int(input()))

ary.sort()
for idx in ary:
    print(idx)