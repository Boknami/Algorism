n, m = list(map(int,input().split()))

hash = {} #파이썬 딕셔너리 이용

for i in range(n):
    site, pw = list(map(str,input().split()))
    hash[site] = pw

print('--------------')

for i in range(m):
    find_site = input()
    print(hash[find_site])
