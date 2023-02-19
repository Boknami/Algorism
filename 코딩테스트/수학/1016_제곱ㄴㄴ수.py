# 1000000000000
mi, ma = map(int, input().split())
ary = []
cnt = 0

if(mi == ma):
    print(1)
else:
    if(ma >= 4):
        for i in range(2, ma):
            print(i, ma)
            a = i * i
            if(a >= ma):
                print('끝', a, i)
                break
            value = a

            # 2의 제곱수인 4로 나누어진다면
            # 16의 제곱수는 할 필요도 없다.
            while(value <= ma):
                if(not ary.__contains__(value)):
                    ary.append(value)
                value += a

    print('--------------')
    print(ma - len(ary))
