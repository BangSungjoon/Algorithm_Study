# [백준] 신나는 함수 실행
def dfs(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dfs(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = dfs(a, b, c-1) + dfs(a, b-1, c-1) - dfs(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = dfs(a-1, b, c) + dfs(a-1, b-1, c) + dfs(a-1, b, c-1) - dfs(a-1, b-1, c-1)
        return dp[a][b][c]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    li = list(map(int, input().split()))
    if li == [-1, -1, -1]:
        break
    x, y, z = li
    print(f'w({x}, {y}, {z}) = {dfs(x, y, z)}')