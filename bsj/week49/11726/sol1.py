# 2xn 타일링

n = int(input())
dp = [0]*(n+2)

dp[1] = 1
dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 8
# dp[6] = 13
# dp[7] = 21
# dp[8] = 34
# dp[9] = 55

if n >= 3:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)