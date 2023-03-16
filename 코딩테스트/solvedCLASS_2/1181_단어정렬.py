import sys
input = sys.stdin.readline()

N = int(input())
words = []

for _ in range(N):
    words.append(input())

# 중복 제거
words = list(set(words))

# 길이 기준 정렬
words.sort()
words.sort(key=len)

# 출력
for word in words:
    print(word)