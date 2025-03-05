# 재귀 dfs로 풀기
def dfs(x, y, cnt):
    """
    말이 최대 몇 칸을 지나는지 구하는 함수
    Args:
        x: x좌표
        y: y좌표
        cnt: 지난 횟수
    """
    global result
    if cnt > result:
        result = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R:
            if visited[ord(arr[ny][nx]) - 65] == 0:
                visited[ord(arr[ny][nx]) - 65] = 1
                dfs(nx, ny, cnt+1)
                visited[ord(arr[ny][nx]) - 65] = 0

# 입력 받기
R, C = map(int, input().split())
arr = [input() for _ in range(R)]
result = 0

visited = [0] * 26
visited[ord(arr[0][0]) - 65] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, 1)
print(result)