N = int(input())

dp = [0] * (N+1) # 최대값이여
score = [0] * (N+1) # 점수판이여

for i in range(1, N+1):
    score[i] = int(input())

# 계단이 1개 또는 2개인 경우
if N == 1:
    print(score[1])
elif N == 2:
    print(score[1] + score[2])
else:
    # 3번째 계단부터 진행하려고 1,2번째 계단 경우 
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    
    # 3번째 계단부터 dp 진행
    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + score[i],  # 최대값에서 두 계단 전에서 현재 계단으로 오는 경우 더하기
                   dp[i-3] + score[i-1] + score[i])  # 최대값에서 세 계단 전에서 이전 계단을 거쳐 현재 계단으로 오는 경우 더하기
    
    # 결과 출력
    print(dp[N])



# 1.i번째 계단과 i-1번째 계단이 연속될 경우
# 2. 연속되지 않게 i번째 계단에 도착할 경우
# 1번 같은 경우에는 i-3번째 계단까지의 최대 합과 더하고, 2번 같은 경우 i-2번째 계단까지의 최대 합과 더한다.