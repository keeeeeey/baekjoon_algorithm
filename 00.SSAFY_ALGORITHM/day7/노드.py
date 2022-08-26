class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Node 를 사용해서 트리 만들어보기

root = Node(1)      # root 노드 만들기

# 2, 3 을 root의 왼쪽과 오른쪽에 추가
root.left = Node(2)
root.right = Node(3)

# 4, 5 를 2번의 왼쪽과 오른쪽에 추가
root.left.left = Node(4)
root.left.right = Node(5)

# 전위순회
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

# 후위순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

preorder(root)
inorder(root)
postorder(root)