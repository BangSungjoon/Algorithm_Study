# 백준 내려가기
# dp
n = int(input())
max_dp = list(map(int, input().split()))
min_dp = max_dp[:]  # 처음 줄

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    max0 = max(max_dp[0], max_dp[1]) + a
    max1 = max(max_dp[0], max_dp[1], max_dp[2]) + b
    max2 = max(max_dp[1], max_dp[2]) + c

    min0 = min(min_dp[0], min_dp[1]) + a
    min1 = min(min_dp[0], min_dp[1], min_dp[2]) + b
    min2 = min(min_dp[1], min_dp[2]) + c

    max_dp = [max0, max1, max2]
    min_dp = [min0, min1, min2]

print(max(max_dp), min(min_dp))