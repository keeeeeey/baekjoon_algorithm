def pre(n):
    if n <= size:
        pre_arr.append(tree[n])
        pre(2 * n)
        pre(2 * n + 1)

def inorder(n):
    if n <= size:
        inorder(2 * n)
        in_arr.append(tree[n])
        inorder(2 * n + 1)

def postorder(n):
    if n <= size:
        postorder(2 * n)
        postorder(2 * n + 1)
        post_arr.append(tree[n])

tree = [0, 1, 2, 3]
size = len(tree) - 1
pre_arr = []
in_arr = []
post_arr = []
pre(1)
inorder(1)
postorder(1)
print(pre_arr)
print(in_arr)
print(post_arr)
answer = []
for i in range(3):
    answer.append(max)
