import sys
input = sys.stdin.readline

def mergeSort(ary):
    #분할
    if(len(ary) < 2): return ary

    mid = len(ary)//2
    leftAry = mergeSort(ary[:mid])
    rightAry = mergeSort(ary[mid:])

    #병합
    LIdx = 0
    RIdx = 0
    mergeAry = []

    #배열에 인덱스를 넘기지 않기 위해서
    while((LIdx < len(leftAry)) and (RIdx < len(rightAry))):
        if(leftAry[LIdx] > rightAry[RIdx]):
            mergeAry.append(rightAry[RIdx])
            RIdx+=1
        else:
            mergeAry.append(leftAry[LIdx])
            LIdx+=1
    
    #남은 걸 합치자
    mergeAry += leftAry[LIdx:]
    mergeAry += rightAry[RIdx:]
    return mergeAry

ary = []
N = int(input())
for i in range(N):
    ary.append(int(input()))

ary = mergeSort(ary)
for value in ary:
    print(value)
