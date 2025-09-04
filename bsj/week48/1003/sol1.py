# [백준] 피보나치 함수
t = int(input())

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    num1 = dp[i-1][0] + dp[i-2][0]
    num2 = dp[i-1][1] + dp[i-2][1]

    dp[i] = [num1, num2]

for test_case in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])