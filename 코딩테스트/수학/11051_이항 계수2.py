def fac(N, k, m):
    global res
    res = 1

    if(m == k): return
    m+=1
    res = res * N
    fac(N-1, k, m)

def fac1(K,m):
    global res2
    res2 = 1

    if(m == K): return
    m+=1
    res2 = res2 * K
    fac1(K+1, m)

N,K = map(int,input().split())
fac(N,K,0)
fac1(K,0)

print(res, res2)