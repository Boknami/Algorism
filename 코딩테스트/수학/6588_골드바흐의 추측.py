import sys
import math

n = 1000000
ary = [True for i in range(n+1)]

while(n != 0):
    n = int(input())
    
    #제곱근까지 반복 진행
    for i in range(2, int(math.sqrt(n)) + 1):
        if(ary[i] == True):
            k = 2

            while (i * k <= n):
                ary[i * k] = False
                k += 1

    for j in range(2, n+1):
        if(ary[j]): print(j, end =' ')