N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
#DP표는 0~K+1, 0~N+1로 구성하자 (N=1일 때, DP[i-1][j]가 존재해야 하므로)

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= bag[i-1][0]:   #현재 최대무게j가 해당 물건무게보다 큰 경후
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j]) # 물건을 조합하기 전에 얻을 수 있는 최대 가치와 현재물건가치+이전물건가치 둘 중 최대값이 dp값이 됨
        else :
            dp[i][j] = dp[i-1][j]

print(dp[N][K])





# https://velog.io/@keynene/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC5-%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-12865-%ED%8F%89%EB%B2%94%ED%95%9C%EB%B0%B0%EB%82%AD