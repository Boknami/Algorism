import sys
sys.setrecursionlimit(10**5)

def factorial(n, cnt, tar):
    if(n > 1 and cnt != tar):
        cnt += 1
        return n * factorial(n-1, cnt, tar)
    else:
        return 1

N,K = map(int,input().split())
s1 = factorial(N,0,K)
s2 = factorial(K,0,K)
s3 = s1//s2

print(int(s3%10007))