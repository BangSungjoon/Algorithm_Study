N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]
dp[0][nums[0]] = 1

for i in range(N-2):
    for j in range(21):
        if dp[i][j]:    # i번째까지 더하거나 뺏을 때 j가 나오는 경우의 수
            if j + nums[i+1] <= 20:
                dp[i+1][j+nums[i+1]] += dp[i][j]
            if j - nums[i+1] >= 0:
                dp[i+1][j-nums[i+1]] += dp[i][j]

print(dp[N-2][nums[-1]])