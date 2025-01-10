# 백준
# 계단 오르기
# DP로 다시 풀기
n = int(input())
step = [0]*n        # 계단
for i in range(n):
    step[i] = int(input())
dp = [0]*n          # dp[i]는 현재 칸까지
                    # 도달하는 최대값

if n < 3:           # 계단 칸 수가 2칸 이하인 경우
    print(sum(step))
else:
    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    dp[2] = max(step[0]+step[2], step[1]+step[2])
    for i in range(3, n):
        dp[i] = max(step[i]+dp[i-2], step[i]+step[i-1]+dp[i-3])

    print(dp[-1])