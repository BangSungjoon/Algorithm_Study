# [백준] DFS와 BFS
def dfs(node):
    dfs_visited[node] = 1
    dfs_result.append(node)
    for idx in adj_l[node]:
        if dfs_visited[idx] == 0:
            dfs(idx)

def bfs(node):
    q = [node]
    bfs_visited[node] = 1
    while q:
        dot = q.pop(0)
        bfs_result.append(dot)
        for idx in adj_l[dot]:
            if bfs_visited[idx] == 0:
                bfs_visited[idx] = 1
                q.append(idx)

# n 정점의 개수, m 간선의 개수, v 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
adj_l = [[] for _ in range(n+1)]

for _ in range(m):
    num1, num2 = map(int, input().split())
    adj_l[num1].append(num2)
    adj_l[num2].append(num1)

for i in range(1, n+1):
    adj_l[i] = sorted(adj_l[i])

dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)
dfs_result = []
bfs_result = []

dfs(v)
bfs(v)
print(*dfs_result)
print(*bfs_result)