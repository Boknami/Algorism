n = int(input())
nList = list(map(int, input().split()))
m = int(input())
listCheck = list(map(int, input().split()))

dict = {}

for value in nList:
    if(value in dict):
        dict[value] += 1
    else:
        dict[value] = 1 

for check in listCheck:
    if(check in dict):
        print(dict[check], end=" ")
    else:
        print(0, end=" ")    