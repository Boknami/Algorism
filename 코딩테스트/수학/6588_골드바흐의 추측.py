import sys
n = 1

while(n != 0):
    n = int(sys.stdin.readline())
    ary = []
    find = 0
    
    if(n%2 != 0):
        continue

    for i in range(2, n-2, 1):
        for j in range(2, i, 1):
            if(i % j == 0):
                break
            if(j == i-1):
                ary.append(i)
    
    for a in ary:
        if(find == 1): break
        for i in range(len(ary)-1, 0, -1):
            if(a + ary[i] == n):
                print(n, '=' ,a,'+', ary[i])
                find = 1
            