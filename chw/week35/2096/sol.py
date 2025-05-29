# 바로 아래의 수 or 바로 아래의 수와 붙어 있는 수로만(위치적으로)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
min_dp = [[0] * 3 for _ in range(N)]

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

min_dp[0][0] = arr[0][0]
min_dp[0][1] = arr[0][1]
min_dp[0][2] = arr[0][2]

for i in range(N):
    for j in range(3):
        if j == 0:
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i-1][j+1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][j], min_dp[i-1][j+1])
        elif j == 1:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][j-1], min_dp[i-1][j], min_dp[i-1][j+1])
        else:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            min_dp[i][j] = arr[i][j] + min(min_dp[i-1][j-1], min_dp[i-1][j])



print(max(dp[N-1]), min(min_dp[N-1]))