# 백준 n과 m (9)
# Trouble Shooting
# `t not in result` 때문에 시간 초과 발생 -> result를 set으로 바꾸고,
# set add를 하기 위해 li를 tuple로 변경 
def dfs(li):
    if len(li) == m:
        t = tuple(li)
        if t not in result:
            result.add(t)
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            dfs(li + [n_list[j]])
            visited[j] = 0

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
visited = [0]*n
result = set()

dfs([])

for i in result:
    print(*i)