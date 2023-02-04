class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # -> None은 아무런 값이 없다라는 의미!

class LiknedList:
    def __init__(self, head_node):
        self.head = head_node

def Add_Node(value):
    cur = LL.head # 헤드부터 시작해서

    # 리스트의 끝으로 이동 후 삽입하자
    while (cur.next != None):
        cur = cur.next

    NN = Node(value)
    cur.next = NN

def Print_Node():
    cur = LL.head # 헤드부터 시작해서

    # 리스트의 끝까지 이동하며 출력
    while (cur.next != None):
        print(cur.value)
        cur = cur.next
    print(cur.value)

def Delete_Node(value):
    cur = LL.head
    if(cur.next == None):
        print('[실패] 남은 노드 : 1 ')
        return

    # 첫 노드를 삭제한다면?
    if(cur.value == value):
        LL.head = cur.next

    # 노드 삭제
    while (cur.next != None):
        if(cur.next.value == value):
            cur.next = cur.next.next
            break
        cur = cur.next
 
# 링크 리스트 초기화
LL = LiknedList(Node(1))

# 노드 추가
for i in range(2, 6):
    Add_Node(i)

Delete_Node(3)
Delete_Node(4)
Delete_Node(1)
Print_Node()