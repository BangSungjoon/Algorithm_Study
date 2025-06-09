# dp 방식으로 풀이(LIS 풀이 찾아봄)

N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N    # dp[i]는 seq[i]가 수열의 마지막 숫자인 수열의 길이

# 수열의 현재 숫자와 그 앞의 숫자들을 비교
# -> 현재 숫자보다 작은 것들이 있다면 해당 숫자가 마지막인 수열의 길이 + 1(현재 숫자가 마지막)
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))