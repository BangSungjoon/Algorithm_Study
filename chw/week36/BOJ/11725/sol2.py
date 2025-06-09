from collections import deque

N = int(input())    # 노드의 갯수
info = [list(map(int, input().split())) for _ in range(N-1)]    # 노드 간 연결 정보

tree = [[] for _ in range(N+1)]     # idx 노드에 연결된 노드들을 기록
res = [0] * (N+1)   # 각 노드의 부모 노드를 기록

for link in info:
    a = link[0]
    b = link[1]
    tree[a].append(b)
    tree[b].append(a)

# 루트 노드부터 시작 - 루트 노드와 연결된 노드를 찾아서 부모 기록 - 부모를 기록한 노드를 큐에 넣고 탐색 반복
def bfs(node):
    q = deque([node])
    while q:
        current = q.popleft()
        for neighbor in tree[current]:
            if res[neighbor] == 0:
                res[neighbor] = current
                q.append(neighbor)

bfs(1)
for i in range(2, N+1):
    print(res[i])