# 백준 내려가기
# dp
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_dp = [[0]*3 for _ in range(n)]
min_dp = [[0]*3 for _ in range(n)]
max_dp[0][:] = min_dp[0][:] = arr[0][:]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            max_dp[i][j] = arr[i][j] + max(max_dp[i-1][0], max_dp[i-1][1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][0], min_dp[i-1][1])
        elif j == 1:
            max_dp[i][j] = arr[i][j] + max(max_dp[i-1][0], max_dp[i-1][1], max_dp[i-1][2])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][0], min_dp[i-1][1], min_dp[i-1][2])
        elif j == 2:
            max_dp[i][j] = arr[i][j] + max(max_dp[i-1][1], max_dp[i-1][2])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][1], min_dp[i-1][2])

print(max(max_dp[n-1]), min(min_dp[n-1]))