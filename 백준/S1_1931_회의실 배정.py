N = int(input())
ary = []

for _ in range(N):
    start, end = map(int, input().split())
    ary.append([start, end])

# 이해 어려웠던 부분
# 종료시간을 기준[빨리 끝나는]으로 정렬하는 건 이해되는데..
# 왜 시작 시간을 기준으로 정렬할까 => 종료 시간이 똑같을 때는 시작 시간이 빠른 것으로 해야 (2,2) 같은 게 실행 가능!
ary = sorted(ary, key = lambda a : a[0])
ary = sorted(ary, key = lambda a : a[1])

End_T = 0 
count = 0

for i, j in ary:
  if i >= End_T:
    count = count + 1
    End_T = j

print(count)

# 실패 풀이
#----------시간 초과----------
# ary.sort()
# max = 0

# for i in range(0, N):
#     end = ary[i][1]
#     room = 1

#     index = ary.index()
    
#     for j in range(i+1, N):
#         if (end <= ary[j][0]):
#             room = room + 1
#             end = ary[j][1]
    
#     if(max < room):
#         max = room
# print(max)
