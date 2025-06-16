# 백준 n과 m (1)
def dfs(li):
    if len(li) == m:
        print(*li)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(li + [n_list[i]])
            visited[i] = 0

n, m = map(int, input().split())
n_list = list(range(1, n+1))
visited = [0]*n

dfs([])