def dfs(graph, start):
    visted = [] #이미 방문
    stack = [start] # (1,2) 방문해야할 스택
    cnt = 0

    # 스택에 꺼낼 게 남아있는동안
    while(stack):
        node = stack.pop() # (3)pop

        # 만약 꺼낸 게 아직 방문하지 않은거라면?
        if (node not in visted):
            cnt+=1
            visted.append(node) # (4) 방문 기록 남기기
            print(cnt , ':' ,  node) # (5) 꺼낸 노드 출력
            stack.extend(graph[node]) # (6) 꺼낸 노드의 자식을 스택에 담자

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

dfs(graph, '식사')