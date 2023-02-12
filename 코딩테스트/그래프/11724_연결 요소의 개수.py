n,m = map(int, input().split())
connect = {}
cnt = 1

for i in range(m):
    u,v = map(int, input().split())

    if i == 0:
        connect[u] = 1
        connect[v] = 1
    else:
        # 딕셔 안에서 값이 존재한다면?
        try:
            if(connect[u]):
                connect[v] = 1
        except:
            print('------------')
            print(u, v)
            print('------------')
            cnt += 1
            connect[u] = 1
            connect[v] = 1
        
print(cnt)