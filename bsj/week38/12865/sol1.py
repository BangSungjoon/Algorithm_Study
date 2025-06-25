# 백준 평범한 배낭
# n: 물품의 수, k: 준서가 버틸 수 있는 무게
# w: 각 물건의 무게, v: 해당 물건의 가치

n, k = map(int, input().split())
product = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(k+1)  # 무게별 물건의 가치 기록

for w, v in product:
    cnt = 0
    for i in range(k, w-1, -1): # 최대 무게부터 그 물건의 무게까지
        cnt += 1
        dp[i] = max(dp[i], dp[i-w]+v)
        # dp[i-w]+v -> 이번 물건의 무게를 뺀 무게 중 최고 가치와 이번 물건의 가치를 더한 값

print(dp[k])