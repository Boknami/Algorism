ary = list(map(int, input('배열 입력 >>').split()))
key = int(input('찾고자 하는 수'))

start = 0
end = len(ary) - 1
mid = 0

while start <= end:
    mid = (start + end) // 2

    # 찾았다
    if(ary[mid] == key):
        print('발견 :', ary[mid])
        break
    # 못찾았다
    elif(ary[mid] < key):
        print('up')
        start = mid + 1
    elif(ary[mid] > key):
        print('down')
        end = mid - 1

