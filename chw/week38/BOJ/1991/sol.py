N = int(input())
tree = [input().split() for _ in range(N)]
tree.sort()

pre_order = ''
in_order = ''
post_order = ''

# 노드 값을 인덱스로 변환
def alphabet(char):
    return ord(char) - 65

# 전위 순회
def pre_ord(T):
    global pre_order

    node = tree[T]

    val = node[0]
    left = node[1]
    right = node[2]

    pre_order += val
    if left != '.': pre_ord(alphabet(left))
    if right != '.': pre_ord(alphabet(right))

# 중위 순회
def in_ord(T):
    global in_order

    node = tree[T]

    val = node[0]
    left = node[1]
    right = node[2]

    if left != '.': in_ord(alphabet(left))
    in_order += val
    if right != '.': in_ord(alphabet(right))

# 후위 순회
def post_ord(T):
    global post_order

    node = tree[T]

    val = node[0]
    left = node[1]
    right = node[2]

    if left != '.': post_ord(alphabet(left))
    if right != '.': post_ord(alphabet(right))
    post_order += val

pre_ord(0)
in_ord(0)
post_ord(0)

print(pre_order)
print(in_order)
print(post_order)