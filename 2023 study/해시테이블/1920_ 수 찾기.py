num = int(input())
nList = list(map(int,input().split()))

dic = {}
for j in range(num):
    dic[nList[j]] = 'value'

find = int(input())
findList = list(map(int,input().split()))

for i in range(find):
    try:
        if(dic[findList[i]]):
            print('1')
    except:
        print('0')