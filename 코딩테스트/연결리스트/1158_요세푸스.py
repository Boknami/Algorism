class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        self.head = value

peo = list(map(int, input().split()))
num = peo[0]
select = peo[1]

for i in range(num + 1):
    if (i == 0): i = 1

    if (i == 1):
        node = Node(i)
        list = LinkedList(node)
    else:
        cur = list.head

        while (cur.next != None):
            cur = cur.next
        
        node = Node(i)
        cur.next = node
    
    if(i == num):
        node.next = list.head

cur = list.head
for j in range(3):
    cur = cur.next
cur