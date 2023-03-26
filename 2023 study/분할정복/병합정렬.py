global cnt
cnt = 0
def mergeSort(arr):
    global cnt
    cnt += 1

    # 최소 길이 1이 되면 return
    if len(arr) < 2: return arr

    mid = len(arr) // 2 # 배열 길이 중간
    left_ary = mergeSort(arr[:mid]) # 좌측
    right_arr = mergeSort(arr[mid:]) # 우측
    
    merged_arr = [] # 최종 담을 배열

    curL = 0
    curH = 0
    while curL < len(left_ary) and curH < len(right_arr):
        if left_ary[curL] < right_arr[curH]:
            merged_arr.append(left_ary[curL])
            curL += 1
        else:
            merged_arr.append(right_arr[curH])
            curH += 1
            
    # 리스트에 남은 걸 합병
    merged_arr += left_ary[curL:] 
    merged_arr += right_arr[curH:]
    return merged_arr

ary = [4,3,2,1]
print(mergeSort(ary))