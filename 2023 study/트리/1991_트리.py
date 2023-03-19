 # 딕셔너리 이용해서 찾는 문제
def preorder(node):
    if(node != None):
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])
    if(node == 'A'): print('')
 
def inorder(node):
    if(node != None):
        inorder(tree[node][0])  # left
        print(node, end='')  # root
        inorder(tree[node][1])  # right
    if(node == 'A'): print('')
 
 
def postorder(node):
    if(node != None):
        postorder(tree[node][0])  # left
        postorder(tree[node][1])  # right
        print(node, end='')  # root
    if(node == 'A'): print('')

tree = {}
n = int(input())

for i in range(n):
    a, b, c = input().split()
    if(b == '.'): b = None
    if(c == '.'): c = None
    tree[a] = [b, c]

preorder('A')
inorder('A')
postorder('A')