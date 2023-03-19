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
            print(i, ma)
            if(a >= ma):
                break
            value = a

            while(value <= ma):
                if(not ary.__contains__(value)):
                    ary.append(value)
                value += a

    print(ma - len(ary))
