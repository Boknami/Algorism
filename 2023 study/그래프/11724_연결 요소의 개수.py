import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def make_dic(p, q):
    if p in graph:
        graph[p].append(q)
    else:
        graph[p] = [q]
        
alredy = []
cnt = 0
def dfs(find):
    # 이미 거친건지 보고 안 거친거면 관련 자식들 빼자
    alredy.append(find)

    # 자식 노드로 계속 파고든다.
    for i in graph[find]:
        if(i in alredy): continue
        else : dfs(i)

vertex, line = map(int, input().split())
graph = {}

for _ in range(line):
    a,b = map(int, input().split())
    make_dic(a, b)
    make_dic(b, a)

keys = list(graph.keys())

for key in keys:
    #이미 방문했다면 넘어가자
    if(key in alredy):
        continue

    dfs(key)
    cnt+=1
remainders = vertex - len(keys)
print(cnt + remainders)