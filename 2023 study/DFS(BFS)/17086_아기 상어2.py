import sys
from collections import deque
input=sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append([a,b,0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    visited[a][b] = True

    while(q):
        cur = q.popleft()

        for i in range(8):
            x = dx[i] + cur[0]
            y = dy[i] + cur[1]
            
            if(0 <= x < row and 0 <= y < col and not visited[x][y]):
                if(cage[x][y] == 1):
                    print(q)
                    return cur[2]
                
                q.append([x,y,cur[2]+1])
                visited[x][y] = True
            
                
row, col = map(int,input().split())
cage = []

dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

for i in range(row):
    cage.append(list(map(int,input().split())))

m_max = 0
temp = 0
for i in range(row):
    for j in range(col):
        if(cage[i][j] == 0):
            temp = bfs(i,j)

            if(m_max < temp):
                m_max = temp
            
print(m_max + 1)

        

