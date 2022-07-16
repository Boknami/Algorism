import sys
input=sys.stdin.readline

i = int(input())
val1 = list(map(int,input().split()))

k = int(input())
val2 = list(map(int,input().split()))

val1.sort()
mid = int(len(val1)/2)

for i in range(k):
    key = val2[i]
    while True:
        if(val1[mid] == key):
            print('1')
            break
        elif(val1[mid] < key):
            print('up')
            mid = int((mid + mid*2) / 2)
        elif(val1[mid] > key):
            print('down')
            mid = int(mid/2)
# k안에 있는 값들 하나씩 꺼내서 i에 있는지 찾아본다.


#입력 받은 k에 값들은 i에 존재하는가?
# for i in range(len(val2)):
#     if(val2[i] in val1):
#         print('1')
#     else:
#         print('0')
