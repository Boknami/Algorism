num = int(input())

for i in range(num):
    stu_score = list(map(int,input().split()))
    stu = stu_score[0]
    del stu_score[0]
    sum = 0

    for k in range(stu):
        sum = sum + stu_score[k]
    avg = sum / stu
    up = 0

    j = 1
    for j in range(stu):
        if(avg < stu_score[j]):
            up = up + 1
    stu_score.clear

    print('%.3f' %((up/stu)*100) + '%')
    
#띄어쓰기로 구분된 여러 숫자 -> map
#list(map(int, input().split() ))

#실수형 표기
# '%.3f' %(숫자)