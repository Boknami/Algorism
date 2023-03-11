import sys
input=sys.stdin.readline

def bfs(a, b):
    q = []
    q.append([a,b,0])

    while(q):
        cur = q.pop()

        for i in range(8):
            x = dx[i] + cur[0]
            y = dy[i] + cur[1]

            if(a==x and b==y):
                continue
            else:
                if(0 <= x <= row-1 and 0 <= y <= col-1 and cage[x][y] == 0 ): 
                    q.append([x,y,cur[2]+1])
            
                if(0 <= x <= row-1 and 0 <= y <= col-1 and cage[x][y] == 1):
                    print(x,y,cur[2])
                    return (cur[2])
        print(q)

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

        

