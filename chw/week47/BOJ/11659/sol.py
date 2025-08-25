N, M = map(int, input().split())
numbers = list(map(int, input().split()))
intervals = [list(map(int, input().split())) for _ in range(M)]

dp = [0] * N
dp[0] = numbers[0]

for i in range(1, len(numbers)):
    dp[i] = dp[i-1] + numbers[i]

for x, y in intervals:
    if x == 1:
        print(dp[y-1])
    else:
        print(dp[y-1] - dp[x-2])