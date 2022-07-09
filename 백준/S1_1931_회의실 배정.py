N = int(input())
ary = []

for _ in range(N):
    start, end = map(int, input().split())
    ary.append([start, end])

ary = sorted(ary, key = lambda a : a[0])
ary = sorted(ary, key = lambda a : a[1]) # 끝 시간 정렬

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
