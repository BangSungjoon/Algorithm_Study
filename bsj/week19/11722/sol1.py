n = int(input())
arr = list(map(int, input().split()))

# dp[i]: i번째 원소를 마지막 원소로 하는 가장 긴 감소 부분 수열의 길이
# 수열은 순서가 있는 집합

dp = [1] * n

# 리스트에서 이전의 index들을 살펴보고 자신보다 큰 놈을 센다.
for i in range(n):          # 0부터 n까지
    for j in range(i):      # 0부터 i까지
        if arr[j] > arr[i]:  # 감소 조건
            dp[i] = max(dp[i], dp[j] + 1)   # dp[i]에 기록
                                            # 내 앞에 나보다 더 큰놈은 max(dp[i], dp[j] + 1)개야
print(max(dp))
