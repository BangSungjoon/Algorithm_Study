# RGB 거리
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = i번째 집이 j색을 선택 했을 때, 최소 비용
dp = [[0]*3 for _ in range(n+1)]
dp[1] = arr[0]
for i in range(2, n+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = arr[i-1][j] + min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] = arr[i-1][j] + min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][j] = arr[i-1][j] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n]))