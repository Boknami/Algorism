import sys
input=sys.stdin.readline

def Bi_find(key, list):
    start = 0
    end = len(list) - 1

    while start <= end :
        mid = (start + end) // 2  
        # 찾았다
        if(list[mid] == key):
            print('1')
            return 1
        # 못찾았다
        elif(list[mid] < key):
            start = mid + 1
        elif(list[mid] > key):
            end = mid - 1
    print('0')

i = int(input())
val1 = list(map(int,input().split()))

k = int(input())
val2 = list(map(int,input().split()))

val1.sort()

for i in range(0, len(val2)):

    Bi_find(val2[i], val1)

# k안에 있는 값들 하나씩 꺼내서 i에 있는지 찾아본다.


#입력 받은 k에 값들은 i에 존재하는가?
# for i in range(len(val2)):
#     if(val2[i] in val1):
#         print('1')
#     else:
#         print('0')
