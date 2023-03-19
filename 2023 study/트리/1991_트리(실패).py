class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None

    def Addnode(self, a, b, c):
        if(self.root == None):
            self.root = Node(a)
            self.root.left = Node(b)
            self.root.right = Node(c)
        else: 
            # 찾은 값을 그냥 함수로 self.FindValue(a)만 하고 a를 바로 사용함.
            # select같은 변수로 받아놓고 select를 써야지.
            k = self.FindValue(self.root, a)
            k.left = b
            k.right = c

    #전위로 값 찾기
    def FindValue(self, node, find):
        if(node.value == find):
            print(node)
            print('이거 찾음?', node.value)
            return node
        if node.left:
            self.FindValue(node.left, find)
        if node.right:
            self.FindValue(node.right, find )

    #전위
    def preorder(self):
        def _preorder(node):
            print(node.value, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    #중위
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.value, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)

    #후위
    def postorder(self):
        def _postorder(node):
            if node.right:
                _postorder(node.right)
            if node.left:
                _postorder(node.left)
            print(node.value, end=' ')
        _postorder(self.root)

N = int(input())
tree = Tree()

for i in range(N):
    a, b, c = input().split()
    tree.Addnode(a, b, c)

tree.preorder()