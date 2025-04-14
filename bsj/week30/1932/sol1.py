# 정수 삼각형
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(i+2) for i in range(1, n+1)]

dp[0][1] = arr[0][0]
for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] = arr[i][j-1] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))