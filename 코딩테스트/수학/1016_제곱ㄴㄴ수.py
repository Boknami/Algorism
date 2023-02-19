# 1000000000000
mi, ma = map(int, input().split())
ary = [True for i in range(ma)]

num = 2
cnt = 0

if(mi == ma):
    print(1)
else:
    if(ma >= 4):
        for i in range(2, ma//2, 1):
            a = i * i
            value = a

            while(value <= ma):
                ary[value-1] = False
                value += a

    for j in range(mi, ma, 1):
        if(not ary[j]):
            cnt += 1

    print('--------------')
    print(ma - cnt)
