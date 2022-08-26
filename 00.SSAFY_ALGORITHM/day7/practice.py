class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

v = int(input())

tree = [Node(i) for i in range(v + 1)]      # 노드는 1번부터 존재

edge_list = list(map(int, input().split()))

# 입력을 두개씩 잘라서 확인
# 앞 ==> 부모 p
# 뒤 ==> 자식 c
while edge_list:
    p = edge_list.pop(0)    # 부모
    c = edge_list.pop(0)    # 자식
    # 입력 처리 (트리 만들기)
    # 부모를 기준으로 왼쪽이 있는 겨 ㅇ우
    if tree[p].left:
        tree[p].right = tree[c]
    else:
        tree[p].left = tree[c]

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

preorder(tree[1])
print()