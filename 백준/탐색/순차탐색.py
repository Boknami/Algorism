# 가장 간단하고 직접적인 탐색
# 탐색 O : (n+1)/2
# 탐색 X : n
def seq_find(list, key):
    for i in range(0, len(list)):
        if(list[i] == key):
            print('발견 => 인덱스 : ', i)
            return 1
    print('못찾았어요..')
    return 0

ary = list(map(int, input('배열 입력 >> ').split()))

seq_find(ary ,int(input('찾고자 하는 수 >> ')))
