N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = [0, 0]
# 비적록색약이 볼 때의 그룹 개수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            answer[0] += 1
# 적록색약이 볼 때의 그룹 개수를 새기 위하여 초록색을 빨간색으로 바꿈
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
# 적록색약약이 볼 때의 그룹 개수
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(None):
        if not visited[i][j]:
            bfs(i, j)
            answer[1] += 1
# 출력은 gpt 참고
print(' '.join(map(str, answer))) 
