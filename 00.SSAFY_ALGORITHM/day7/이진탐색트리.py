class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BinarySearchTree
class BST:
    def __init__(self):
        self.root = None    # root는 트리의 시작지점

    # 탐색 연산
    def search(self, target):
        now = self.root     # 탐색의 시작은 root 부터
        cnt = 0
        # 찾을때까지 반복 (노드가 없어질 때까지)
        while now:
            # 현재 내가 있는 노드의 키값과 찾고있는 값이 같으면 반환
            if target == now.data:
                print(cnt)
                return now
            # 내가있는 노드의 키값이 찾고있는 값보다 작으면 왼쪽으로 이동
            elif target < now.data:
                now = now.left
            # 내가있는 노드의 키값이 찾고있는 값보다 크면 오른쪽으로 이동
            elif target > now.data:
                now = now.right
            cnt += 1
        # 만약 반복이 끝나버렸다. ==> 찾는 데이터가 이진 탐색 트리 안에 없다.
        return now

    def insert(self, node):
        now = self.root     # root 부터 탐색 시작

        # 루트 노드가 없다면 바로 리턴
        if now == None:
            self.root = node        # 제일 처음 들어온 노드가 로트 노드가 된다.
            return

        # 탐색을 진행해서 탐색 실패한 지점에 노드를 삽입
        while True:
            p = now
            # 넣고싶은 데이터가 현재 노드보다 작으면 왼쪽
            if node.data < now.data:
                now = now.left
                if not now:
                    p.left = node
                    return
            else:
                now = now.right
                if not now:
                    p.right = node
                    return

# root = Node(9)
# root.left = Node(4)
# root.right = Node(12)
# root.left.left = Node(3)
# root.left.right = Node(6)
# root.right.right = Node(15)
# root.right.right.left = Node(13)
# root.right.right.right = Node(17)

bst = BST()
# bst.root = root
# bst.search(13)
# bst.insert(Node(5))
data_list = list(map(int, input().split()))
node_list = [Node(i) for i in data_list]
for node in node_list:
    bst.insert(node)

bst.search(9)
bst.search(4)
bst.search(15)
bst.search(17)