import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(scores[0][0], scores[1][0]))
    else:
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = scores[0][0]
        dp[1][0] = scores[1][0]
        dp[0][1] = scores[0][1] + scores[1][0]
        dp[1][1] = scores[1][1] + scores[0][0]

        for i in range(2, n):
            dp[0][i] = scores[0][i] + max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] = scores[1][i] + max(dp[0][i - 1], dp[0][i - 2])

        print(max(dp[0][n-1], dp[1][n-1]))