num = int(input())

for i in range(num):
    ary = []
    ary.append(input())
    sum = 0
    
    flag = 0
    n = 1
    for j in range(len(ary[0])):
        if(ary[0][j] == 'O'):
            if(flag == 1):
                n = n + 1
                sum = sum + n
            else :
                flag = 1
                sum = sum + n
        else:
            flag = 0
            n = 1
    print(sum)
