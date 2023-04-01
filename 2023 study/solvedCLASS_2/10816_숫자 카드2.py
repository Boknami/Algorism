n = int(input())
nList = list(map(int, input().split()))
m = int(input())
listCheck = list(map(int, input().split()))

for idx in listCheck:
    print(nList.count(idx), end=" ")    