dp = [0] * 11  # 11자리까지 나타낼 방법개수
dp[0] = 1  
dp[1] = 1  
dp[2] = 2  
dp[3] = 4  

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])
