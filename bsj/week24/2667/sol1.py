# 단지 번호 붙이기

# dfs로 풀자
def dfs(x, y):
    """
    아파트 단지를 찾으면, 돌면서 집의 수 세는 함수

    Args:
        x: x좌표
        y: y좌표
    """
    global n, size
    if town[y][x] == '0':
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and town[ny][nx] == '1':
            visited[ny][nx] = 1
            size += 1
            dfs(nx, ny)


# 입력 받기
n = int(input()) # 정사각형 지도 n*n
town = [input() for _ in range(n)] # 문자열로 받았음
result = [] # 단지내 집의 수를 기록할 리스트
visited = [[0]*n for _ in range(n)]
size = 0 # 현재 돌고 있는 단지 내 집의 수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if town[i][j] == '1' and visited[i][j] == 0:
            size = 1
            visited[i][j] = 1
            dfs(j, i)
            result.append(size)
result.sort()
print(len(result))
for r in result:
    print(r)