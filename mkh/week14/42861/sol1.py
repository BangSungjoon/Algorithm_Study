def solution(n, costs):
    adj = [[0] * n for _ in range(n)]
    for cost in costs:
        s, e, c = cost
        adj[s][e] = adj[e][s] = c
    min_cost = float('inf')

    def dfs(curr, cost, visited, poss_go):
        nonlocal min_cost
        if cost > min_cost:
            return
        elif len(visited) == n:
            min_cost = cost
        else:
            for i in range(n):
                if adj[curr][i] and i not in visited:
                    poss_go.append((curr,i))
            while poss_go:
                go, next = poss_go.pop()
                if next not in visited:
                    dfs(next, cost + adj[go][next], visited + [next], poss_go.copy())

    dfs(0, 0, [0], [])  # 시작점, 총 코스트, 방문배열

    return min_cost

solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])