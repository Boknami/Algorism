M = int(input())
N = int(input())
sema = 0

for i in range(M, N, 1):
    sema = 0
    for j in range(2, M):
        if(M % j == 0):
            sema = 1
            break
    if(sema == 0):
        print(M)
    M = M + 1    