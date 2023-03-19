# 딕셔너리를 이용해서 해당 숫자가 몇 번째 인지 저장하는 건 어때
n = int(input())
ary = list(map(int,input().split()))
ary2 = ary[:]
ary2 = list(set(ary2))
ary2.sort()

dic = {}
for i in range(n):
    dic[ary[i]] = 0

for j in range(len(ary2)): 
    if dic[ary2[j]] == 0:
        dic[ary2[j]] = j

for k in range(n):
    print(dic[ary[k]], end=' ')