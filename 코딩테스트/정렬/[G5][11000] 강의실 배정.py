def check()

n = int(input())
q = []

for i in range(n):
    s, e = map(int, input().split())
    q.append([s, e])

q.sort()

# 가장 빠른 시간부터 강의 시작
# 만약 겹치는 강의 시간이 있다면 그 강의 시간으로 연강
cnt = 0

while q:
    start = q.pop(0)
    cnt += 1
    end = start[1]

    find = 0
    for i in range(len(q)):
        if(q[i][0] == end): # 시작 시간이 첫 강의에 끝이랑 맞아 떨어진다면?
            find += 1
            if(find >= 1):
                q.pop(i)

print(cnt)