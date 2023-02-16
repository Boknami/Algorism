from sys import stdin

ary = [True for i in range(1000001)]

for i in range(2, 1001):
    if ary[i]:
        for k in range(i + i, 1000001, i):
            ary[k] = False

while True:
    n = int(stdin.readline())

    if n == 0: break

    for i in range(3, len(ary)):
        if ary[i] and ary[n-i]:
            print(n, "=", i, "+", n-i)
            break