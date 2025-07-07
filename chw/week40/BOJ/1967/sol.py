import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
info = [list(map(int, input().split())) for _ in range(n-1)] # 부모, 자식, 가중치
tree = [[] for _ in range(n+1)] # 1~n번 노드까지

for data in info:
    parent = data[0]
    child = data[1]
    weight = data[2]

    # 양방향 연결
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

# 가장 먼 노드 찾은 후 거리 저장
def dfs(node, length, visited):
    global max_w, last_node

    visited[node] = 1

    if length > max_w:
        max_w = length
        last_node = node

    for next_node, w in tree[node]:
        if not visited[next_node]:
            dfs(next_node, length+w, visited)

# 가장 먼 노드 찾기
max_w = 0
last_node = 0
dfs(1, 0, [0]*(n+1))

# 가장 먼 노드에서 다시 가장 먼 노드 찾기
max_w = 0
dfs(last_node, 0, [0]*(n+1))

print(max_w)