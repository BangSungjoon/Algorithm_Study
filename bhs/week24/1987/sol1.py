def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if nx <= -1 or nx >= R or ny <= -1 or ny >= C:
            continue

        if visited[ord(graph[nx][ny]) - 65] == 0:
            visited[ord(graph[nx][ny]) - 65] = 1
            dfs(nx, ny, count+1)
            visited[ord(graph[nx][ny]) - 65] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(str, input())))

visited = [0] * 26
visited[ord(graph[0][0])-65] = 1

answer = 1

dfs(0, 0, 1)

print(answer)