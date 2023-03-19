paper = [[0 for j in range(100)] for i in range(100)]
p_num= int(input())

for i in range(p_num):
  p = list(map(int, input().split()))
  j = 0
  k = 0

  for j in range(10):
    for k in range(10):

        paper[p[0] + j][p[1] + k] = 1

sum = 0
for N in range(100):
    for M in range(100):
        if(paper[N][M] == 1):
            sum = sum + 1

print(sum)