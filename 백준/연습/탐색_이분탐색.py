ary = list(map(int, input('배열 입력 >>').split()))
key = int(input('찾고자 하는 수'))

# 현 배열에서 중간
div = int(len(ary)/2)
print(div)

while True:
    # 찾았다
    if(ary[div] == key):
        print('발견 :', ary[div])
        break
    # 못찾았다
    elif(ary[div] < key):
        print('up')
        div = int((div + div*2) / 2)
    elif(ary[div] > key):
        print('down')
        div = int(div/2)

