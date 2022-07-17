def binary_find(key):    
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        # 찾았다
        if(ary[mid] == key):
            print('발견 :', ary[mid])
            return 1
        # 못찾았다
        elif(ary[mid] < key):
            print('up')
            start = mid + 1
        elif(ary[mid] > key):
            print('down')
            end = mid - 1
    print('해당 숫자는 존재 X')
    return -1

ary = list(map(int, input('배열 입력 >> ').split()))
binary_find(int(input('찾고자 하는 수 >> ')))