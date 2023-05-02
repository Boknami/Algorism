Node, line, start = map(int,input().split())
graph = [ [0] * (Node+1) for i in range(Node+1) ]

for _ in range(line):
    s,e = map(int,input().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0] * (Node+1)
visited2 = [0] * (Node+1)

#DFS
def DFS(Value):
    visited2[Value] = 1
    print(Value, end=" ")
    for i in range(1, Node+1):
        if (not visited2[i] and graph[Value][i]):
            DFS(i)

#BFS
def BFS(Value):
    q = [Value] 
    visited[Value] = 1
    while q:
        value = q.pop(0)
        print(value, end = " ")
        for i in range(1, Node+1):
            if (not visited[i] and graph[value][i]):#방문하지 않았고, 해당 값과 연결된 값 찾기
                q.append(i)
                visited[i] = 1

DFS(start)
print()
BFS(start)
