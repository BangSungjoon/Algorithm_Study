T = int(input())
for _ in range(T):
    N, coins, M = int(input()), list(map(int, input().split())), int(sys.stdin.readline())
    dp = [0]*(M+1)
    dp[0] = 1 # 0원으로 만드는 가지 수 1개
    for coin in coins:
        for money in range(M+1):
            if money >= coin: # 금액이 동전보다 크면
                dp[money] += dp[money-coin] # 해당 dp는 금액 - 동전에 해당하는 dp합
    print(dp[M])



# dp[money]는 money 금액을 만들 수 있는 경우의 수
# money-coin 금액을 만들어둔 상태에서 coin 동전 하나를 추가하면 money 금액 완성
# 7원을 만들려고 5원을 사용할 것이라면, 2원을 만들 수 있는 경우의 수에 5원까지 하나 추가
# 그러면 dp[7]에는 dp[2]의 경우의 수가 그대로 추가

# 그러면 dp[money] += dp[money-coin]이 됨