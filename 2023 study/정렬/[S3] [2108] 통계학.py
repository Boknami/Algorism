import sys
input=sys.stdin.readline

num = int(input())
ary = []
b_sur = int(num/2)

for i in range(num):
    ary.append(int(input()))
ary.sort()

# 연산 시작
avg = round(sum(ary)/num)
mid_value = ary[b_sur]
ranges = ary[-1] - ary[0]

##########################################
# 최빈값 구하기
dic = {}
ary_cp = ary[:]
ary_cp = list(set(ary_cp))

for i in range(len(ary_cp)):
    dic[ary_cp[i]] = 0

for j in range(num):
    dic[ary[j]] += 1

mx=max(dic.values())#빈도수 중 최대값 구하기

if(mx == 1 and len(ary) == 1):
    most_v = ary[0]
elif(mx == 1 and len(ary) > 1):
    most_v = ary[1]
else:
    mx_dic=[]
    for i in dic:
        if mx == dic[i]:#딕셔너리 안에 키 값 (i) 가져와서
            mx_dic.append(i)

    if len(mx_dic)>1:
        most_v = mx_dic[1]
    else:
        most_v = mx_dic[0]
print('---')
print(avg)
print(mid_value)
print(most_v)
print(ranges)