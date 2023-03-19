visted = []
def re_dfs(graph, cur):
    visted.append(cur) #현재 노드를 방문했다고 체크해두자.

    # 현재 노드의 자식들을 뽑자
    # 밑에까지 다 탐색하고 다시 올라와서 다른쪽
    for node in graph[cur]:
        if node not in visted: # 방문하지 않은 노드라면?
            print('현재: ', node)
            re_dfs(graph, node)
    
# 그래프 생성
graph = dict()
 
graph['식사'] = ['한식', '중식']
graph['한식'] = ['식사','밥', '면']
graph['중식'] = ['식사','짬뽕', '짜장']
graph['밥'] = ['한식', '된찌', '김찌']
graph['면'] = ['한식','멸치국수']
graph['멸치국수'] = ['면']
graph['짬뽕'] =['중식']
graph['짜장'] =['중식']
graph['김찌'] =['밥']
graph['된찌'] =['밥']

re_dfs(graph, '식사')
print(visted)

# 방문 : 식사, 