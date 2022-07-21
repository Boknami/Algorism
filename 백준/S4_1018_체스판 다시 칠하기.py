# 1. 체스판 입력
N, M = map(int, input().split())
board = []
repaint_list = []

for _ in range(N):
    board.append(input())

# 2. 체스판 경우의 수 모두 탐색
# 8*8 보다 크다면 칸을 이동하며 8*8 크기에서 탐색 
for i in range(0, N - 7):
    for j in range(0, M - 7):
        # 체스판의 시작이 흰색일수도, 검정일수도..
        start_white = 0
        start_black = 0

        # 8*8 크기로 탐색 진행
        for k in range(i, i+8):
            for m in range(j, j+8):
                if (k+m) % 2 == 0:
                    if board[k][m] != 'W':
                        start_white += 1
                    if board[k][m] != 'B':
                        start_black += 1
                else:
                    if board[k][m] != 'B':
                        start_white += 1
                    if board[k][m] != 'W':
                        start_black += 1
        repaint_list.append(min(start_white, start_black))


print(min(repaint_list))
