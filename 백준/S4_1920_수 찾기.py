import sys
input=sys.stdin.readline

i = int(input())
val1 = list(map(int,input().split()))

k = int(input())
val2 = list(map(int,input().split()))

#입력 받은 k에 값들은 i에 존재하는가?
for i in range(len(val2)):
    if(val2[i] in val1):
        print('1')
    else:
        print('0')

    # result = 0
    # for j in range(len(val1)):
    #     if (val2[i] == val1[j]):
    #         print('1')
    #         result = 1
    #         break

    # if (result == 0):
    #     print('0')