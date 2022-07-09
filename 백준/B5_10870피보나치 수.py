n = int(input())
a = 0
b = 1
c = 0

if n == 0:
    print(0)

elif n == 1:
    print(1)

elif (n >= 2):
    for i in range(0, n-1):
        c = a + b
        a = b
        b = c
    print(b)