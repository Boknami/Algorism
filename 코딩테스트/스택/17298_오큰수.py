n = int(input())
stack = list(map(int,input().split()))

for i in range(n):
    temp_s = stack[:]

    # 해당 번째 인덱스를 팝
    value = temp_s.pop(i)
    # while문으로 해당 번째 인덱스 팝하고
    while(temp_s):
        if(i == n-1):
            print('-1')
            break

        compare_v = temp_s.pop(i)

        #print(value,':',compare_v)
        if(value < compare_v):
            print(compare_v, end=' ')
            break

        # 못 찾고 종료
        if(len(temp_s) == i):
            print('-1', end=' ')
            break
    